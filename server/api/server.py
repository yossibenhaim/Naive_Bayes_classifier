from fastapi import FastAPI
from sklearn.model_selection import train_test_split
from model.Test_for_classifier import Test_classifier
from model.Probability_Classifier import Probability
from data.Cleaning_data import Cleaning_data
from data.load_csv import LoadCsv
from pydantic import BaseModel
import pandas as pd

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
    Loads a CSV file from a given URL and saves it to the local system.

    Args:
        url (CsvUrl): An object containing the URL of the CSV file.

    Returns:
        dict: Empty dictionary on success.
    """
    csv = LoadCsv()
    data = csv.load_csv(url.url)
    csv.saving_data_csv(data)
    global _test_data_global
    _test_data_global = None
    return {}


@app.post("/csv/columns")
def clean_data_from(column: CsvColumn):
    """
    Sets the specified column as the index of the loaded CSV data.

    Args:
        column (CsvColumn): Object with the column name to set as index.

    Returns:
        dict: Empty dictionary on success.
    """
    csv = LoadCsv()
    clean = Cleaning_data(csv.read_data_csv())
    new_data = clean.cleaning_data(column.column)
    csv.saving_data_csv(new_data)
    global _test_data_global
    _test_data_global = None
    return {}


@app.post("/model/train")
def post_probability():
    """
    Trains a Naive Bayes classifier on the loaded dataset and saves the result.

    Returns:
        dict: Empty dictionary on success.
    """
    csv = LoadCsv()
    full_data = csv.read_data_csv()
    train_data, test_data = train_test_split(full_data, test_size=0.3, random_state=42)
    global _test_data_global
    _test_data_global = test_data
    probability = Probability()
    probability_data = probability.create_probability(train_data)
    csv.saving_probability(probability_data)
    return {}


@app.post("/model/test")
def test_probability():
    """
    Evaluates the classifier's accuracy on the current dataset.

    Returns:
        dict: Dictionary containing the accuracy result.
    """
    csv = LoadCsv()
    probability_data = csv.read_probability_dict()
    test = Test_classifier(probability_data, _test_data_global)
    result = test.test(_test_data_global)
    return {"result": result}


@app.get("/csv/preview")
def return_data_frame():
    """
    Returns the current dataset as a list of dictionaries for preview.

    Returns:
        dict: A dictionary with the dataset and index column name.
    """
    csv = LoadCsv()
    data = csv.read_data_csv()
    name_index = data.index.name
    if name_index is None:
        name_index = "index"
    return {"result": data.reset_index().to_dict("records"), "name_index": name_index}


@app.get("/probability")
def return_probability():
    """
    Returns the current dataset as a list of dictionaries for preview.

    Returns:
        dict: A dictionary with the dataset and index column name.
    """
    csv = LoadCsv()
    probability_data = csv.read_probability_dict()
    return {"result": probability_data}
