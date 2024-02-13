#!/usr/bin/python3

# This is the test file for the base_model.py

from models.base_model import BaseModel

model = BaseModel()
model.number = 89
model.name = "My 1st model"
print(f"{model}")
model.store()
print(f"{model}")
model_json = model.dictionary()
print(f"{model_json}")
print(f"Model's JSON")
for key in model_json.keys():
    print(f"\t{key}: ({type(model_json[key])}) - {model_json[key]}")
