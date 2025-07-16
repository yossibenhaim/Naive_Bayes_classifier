from fastapi import FastAPI
from server.Probability_Classifier import Probability
from server.Test_for_classifier import Test_classifier
from server.Cleaning_data import Cleaning_data
from server.load_csv import LoadCsv
from pydantic import BaseModel

app = FastAPI()


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
    return {}


@app.post("/model/train")
def post_probability():
    """
    Trains a Naive Bayes classifier on the loaded dataset and saves the result.

    Returns:
        dict: Empty dictionary on success.
    """
    csv = LoadCsv()
    data = csv.read_data_csv()
    probability = Probability()
    probability_data = probability.create_probability(data)
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
    data_frame = csv.read_data_csv()
    test = Test_classifier(probability_data, data_frame)
    result = test.test(data_frame)
    return {"result": result}


@app.post("/model/check")
def check_probability(dict_row: RowInput):
    """
    Classifies a new row based on user input using the trained model.

    Args:
        dict_row (RowInput): Object containing a dictionary of values to classify.

    Returns:
        dict: Dictionary containing the predicted class.
    """
    csv = LoadCsv()
    probability_data = csv.read_probability_dict()
    data_frame = csv.read_data_csv()
    test = Test_classifier(probability_data, data_frame)
    result = test.check_probability(dict_row.row)
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
    if name_index:
        return {"result": data.reset_index().to_dict("records"), "name_index": name_index}
    else:
        return {"result": data.reset_index().to_dict("records"), "name_index": "index"}
