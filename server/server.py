import pandas
from fastapi import FastAPI
from Probability_Classifier import Probability
from Test_for_classifier import Test_classifier
from Cleaning_data import Cleaning_data
from pydantic import BaseModel
from typing import List, Dict, Any


app = FastAPI()




class DataFrameInput(BaseModel):
    data_frame: List[Dict[str, Any]]

class DataDictInput(BaseModel):
    data_dict: Dict[str, Dict[str, Dict[str, Dict[str, float]]]]
    data_frame: List[Dict[str, Any]]

class CheckInput(BaseModel):
    data_dict: Dict[str, Dict[str, Dict[str, Dict[str, float]]]]
    dict_row: Dict[str, Dict[str, str]]

@app.post("/clean_data")
def clean_data_from(data : DataFrameInput):
    df = pandas.DataFrame(data.data_frame)
    clean = Cleaning_data()
    new_data = clean.cleaning_data(df)
    return {"result":new_data}

@app.post("/probability")
def get_probability(data : DataFrameInput):
    df = pandas.DataFrame(data.data_frame)
    probability = Probability()
    return {"result":probability.create_probability(df)}

@app.post("/test")
def test_data(data : DataDictInput):
    test = Test_classifier(data.data_dict)
    return {"result":test.test(data.data_frame)}

@app.post("/check")
def check_probability(input_data: CheckInput):
    test = Test_classifier(input_data.data_dict)
    return {"result":test.check_probability(input_data.dict_row)}