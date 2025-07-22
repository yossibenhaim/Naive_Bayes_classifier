from fastapi import FastAPI
from ..probability_model.classified_probability import Classifier
from pydantic import BaseModel
import requests
import pandas as pd
from io import StringIO

app = FastAPI()
classifier = None


class CsvUrl(BaseModel):
    """
    Model containing the URL to a CSV file.

    Args:
        url (str): CSV file URL.
    """
    url: str


class RowInput(BaseModel):
    """
    Model for a data row to classify.

    Args:
        row (dict): Dictionary of column-value pairs.
    """
    row: dict


@app.post("/read/classified")
def read_classified(url: CsvUrl):
    """
    Initialize classifier using probabilities and CSV data.

    Args:
        url (CsvUrl): URL to CSV file (currently unused).

    Returns:
        dict: Confirmation message.
    """
    global classifier
    classified = requests.get("http://127.0.0.1:8050/probability").json()
    data = requests.get("http://127.0.0.1:8050/csv/preview").text
    data_frame = pd.read_csv(StringIO(data))
    classifier = Classifier(classified, data_frame)
    return {"message": "Classifier initialized"}


@app.post("/model/check")
def check_probability(dict_row: RowInput):
    """
    Classify a new data row.

    Args:
        dict_row (RowInput): Input data row.

    Returns:
        dict: Classification result.
    """
    global classifier
    if classifier is None:
        read_classified(CsvUrl(url="http://127.0.0.1:8050/data.csv"))
    result = classifier.check_probability(dict_row.row)
    return {"result": result}
