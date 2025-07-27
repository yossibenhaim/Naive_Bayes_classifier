from fastapi import FastAPI, HTTPException
from probability_model.classified_probability import Classifier
from pydantic import BaseModel
import requests
import pandas as pd
import logging

app = FastAPI()
classifier = None

logging.basicConfig(
    level=logging.INFO,
    filename="logs/api.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CsvUrl(BaseModel):
    """
    Pydantic model representing a CSV URL input.

    Attributes:
        url (str): URL pointing to the CSV file.
    """
    url: str


class RowInput(BaseModel):
    """
    Pydantic model representing a single data row for classification.

    Attributes:
        row (dict): Dictionary with column-value pairs representing a data row.
    """
    row: dict


@app.get("/read/classified")
def read_classified():
    """
    Initialize the Naive Bayes classifier by fetching probabilities and dataset from an external service.

    Returns:
        dict: Confirmation message upon successful initialization.

    Raises:
        HTTPException: If external requests fail or data processing encounters an error.
    """
    global classifier
    try:
        logger.info("Fetching classified probabilities from external service.")
        classified_response = requests.get("http://naive-bayes-container-server:8000/probability", timeout=10)
        classified_response.raise_for_status()
        classified = classified_response.json()

        logger.info("Fetching CSV preview data from external service.")
        data_response = requests.get("http://naive-bayes-container-server:8000/csv/preview", timeout=10)
        data_response.raise_for_status()
        data = data_response.json()

        data_frame = pd.DataFrame(data["result"])
        data_frame = data_frame.set_index(data["name_index"])

        classifier = Classifier(classified["result"], data_frame)
        logger.info("Classifier initialized successfully.")
        return {"message": "Classifier initialized"}

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error during classifier initialization: {e}")
        raise HTTPException(status_code=503, detail="Failed to fetch data from external service.")

    except (KeyError, ValueError) as e:
        logger.error(f"Data processing error during classifier initialization: {e}")
        raise HTTPException(status_code=500, detail="Invalid data received from external service.")

    except Exception as e:
        logger.error(f"Unexpected error during classifier initialization: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during classifier initialization.")


@app.post("/model/check")
def check_probability(dict_row: RowInput):
    """
    Classify a new input data row using the initialized classifier.

    Args:
        dict_row (RowInput): Input data row containing column-value pairs.

    Returns:
        dict: Classification probabilities result.

    Raises:
        HTTPException: If classifier is not initialized or classification fails.
    """
    global classifier
    try:
        if classifier is None:
            logger.info("Classifier not initialized; initializing now.")
            read_classified()

        result = classifier.check_probability(dict_row.row)
        logger.info("Classification performed successfully.")
        return {"result": result}

    except Exception as e:
        logger.error(f"Error during classification: {e}")
        raise HTTPException(status_code=500, detail="Failed to classify input data.")
