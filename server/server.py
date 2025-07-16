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
    csv = LoadCsv()
    data = csv.load_csv(url.url)
    csv.saving_data_csv(data)
    return {}

@app.post("/csv/columns")
def clean_data_from(column:CsvColumn):
    csv = LoadCsv()
    clean = Cleaning_data(csv.read_data_csv())
    new_data = clean.cleaning_data(column.column)
    csv.saving_data_csv(new_data)
    return {}

@app.post("/model/train")
def post_probability():
    csv = LoadCsv()
    data = csv.read_data_csv()
    probability = Probability()
    probability_data = probability.create_probability(data)
    csv.saving_probability(probability_data)
    return {}

@app.post("/model/test")
def test_probability():
    csv = LoadCsv()
    probability_data = csv.read_probability_dict()
    data_frame = csv.read_data_csv()
    test = Test_classifier(probability_data, data_frame)
    result = test.test(csv.read_data_csv())
    return {"result": result}

@app.post("/model/check")
def check_probability(dict_row : RowInput):
    csv = LoadCsv()
    probability_data = csv.read_probability_dict()
    data_frame = csv.read_data_csv()
    test = Test_classifier(probability_data, data_frame)
    result = test.check_probability(dict_row.row)
    return {"result":result}

@app.get("/csv/preview")
def return_data_frame():
    csv = LoadCsv()
    data = csv.read_data_csv()
    name_index = data.index.name
    if name_index:
        return {"result": data.reset_index().to_dict("records"), "name_index": name_index}
    else:
        return {"result": data.reset_index().to_dict("records"), "name_index": "index"}
