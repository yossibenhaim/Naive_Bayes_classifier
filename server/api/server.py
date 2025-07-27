from fastapi import FastAPI, HTTPException
from sklearn.model_selection import train_test_split
from model.Test_for_classifier import Test_classifier
from model.Probability_Classifier import Probability
from data.Cleaning_data import Cleaning_data
from data.load_csv import LoadCsv
from pydantic import BaseModel
import pandas as pd
import logging

main_server_logger = logging.getLogger("main_server_logger")
main_server_logger.setLevel(logging.INFO)
fh = logging.FileHandler("/server/logs/main_server.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
main_server_logger.addHandler(fh)

main_server_logger.info("Main server started.")

app = FastAPI()

_test_data_global: pd.DataFrame = None


class CsvUrl(BaseModel):
    url: str


class CsvColumn(BaseModel):
    column: str


class RowInput(BaseModel):
    row: dict


@app.post("/csv/load")
def read_csv(url: CsvUrl):
    """
    Load CSV from URL and save locally.

    Args:
        url (CsvUrl): Contains the CSV URL.

    Returns:
        dict: Empty dict on success.

    Raises:
        HTTPException: If loading or saving CSV fails.
    """
    try:
        csv = LoadCsv()
        data = csv.load_csv(url.url)
        csv.saving_data_csv(data)
        global _test_data_global
        _test_data_global = None
        main_server_logger.info(f"CSV loaded and saved from URL: {url.url}")
        return {}
    except Exception as e:
        main_server_logger.error(f"Failed to load or save CSV from {url.url}: {e}")
        raise HTTPException(status_code=500, detail="Failed to load or save CSV.")


@app.post("/csv/columns")
def clean_data_from(column: CsvColumn):
    """
    Set a specified column as index and clean data.

    Args:
        column (CsvColumn): Column to set as index.

    Returns:
        dict: Empty dict on success.

    Raises:
        HTTPException: If cleaning or saving fails.
    """
    try:
        csv = LoadCsv()
        data = csv.read_data_csv()
        clean = Cleaning_data(data)
        new_data = clean.cleaning_data(column.column)
        csv.saving_data_csv(new_data)
        global _test_data_global
        _test_data_global = None
        main_server_logger.info(f"Set column '{column.column}' as index and cleaned data.")
        return {}
    except Exception as e:
        main_server_logger.error(f"Failed to clean data using column '{column.column}': {e}")
        raise HTTPException(status_code=500, detail="Failed to clean data.")


@app.post("/model/train")
def post_probability():
    """
    Train Naive Bayes model on dataset, save probabilities, and keep test set.

    Returns:
        dict: Empty dict on success.

    Raises:
        HTTPException: If training or saving probabilities fails.
    """
    try:
        csv = LoadCsv()
        full_data = csv.read_data_csv()
        train_data, test_data = train_test_split(full_data, test_size=0.3, random_state=42)
        global _test_data_global
        _test_data_global = test_data
        probability = Probability()
        probability_data = probability.create_probability(train_data)
        csv.saving_probability(probability_data)
        main_server_logger.info(
            f"Model trained and probabilities saved. Train size: {len(train_data)}, Test size: {len(test_data)}")
        return {}
    except Exception as e:
        main_server_logger.error(f"Failed to train model or save probabilities: {e}")
        raise HTTPException(status_code=500, detail="Failed to train model.")


@app.post("/model/test")
def test_probability():
    """
    Evaluate classifier accuracy on the test set.

    Returns:
        dict: Contains accuracy result.

    Raises:
        HTTPException: If testing fails or test data is missing.
    """
    try:
        global _test_data_global
        if _test_data_global is None:
            main_server_logger.error("Test data not available. Train model first.")
            raise HTTPException(status_code=400, detail="Test data not available. Train model first.")

        csv = LoadCsv()
        probability_data = csv.read_probability_dict()
        test = Test_classifier(probability_data, _test_data_global)
        result = test.test(_test_data_global)
        main_server_logger.info(f"Model tested. Accuracy result: {result}")
        return {"result": result}
    except HTTPException:
        raise
    except Exception as e:
        main_server_logger.error(f"Failed to test model: {e}")
        raise HTTPException(status_code=500, detail="Failed to test model.")


@app.get("/csv/preview")
def return_data_frame():
    """
    Return the current dataset for preview.

    Returns:
        dict: Dataset as list of dicts and index column name.

    Raises:
        HTTPException: If reading data fails.
    """
    try:
        csv = LoadCsv()
        data = csv.read_data_csv()
        name_index = data.index.name or "index"
        main_server_logger.info("Returning dataset preview.")
        return {"result": data.reset_index().to_dict("records"), "name_index": name_index}
    except Exception as e:
        main_server_logger.error(f"Failed to return dataset preview: {e}")
        raise HTTPException(status_code=500, detail="Failed to return dataset preview.")


@app.get("/probability")
def return_probability():
    """
    Return the current probability dictionary.

    Returns:
        dict: Probability data.

    Raises:
        HTTPException: If reading probability data fails.
    """
    try:
        csv = LoadCsv()
        probability_data = csv.read_probability_dict()
        main_server_logger.info("Returning probability dictionary.")
        return {"result": probability_data}
    except Exception as e:
        main_server_logger.error(f"Failed to return probability dictionary: {e}")
        raise HTTPException(status_code=500, detail="Failed to return probability dictionary.")
