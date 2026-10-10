from pathlib import Path
import json

payload_path = Path(__file__).resolve().parent.parent/"payload_data"

schema_path = Path(__file__).resolve().parent.parent/"payload_schema"


def get_payload_data(payload_file:str):
    payload = payload_path / payload_file
    with open(file=payload, mode="r") as data:
        json_data = json.load(data)
    return json_data

def get_json_schema(schema_file:str):
    schema = schema_path / schema_file
    with open(file=schema, mode="r") as data:
        json_schema = json.load(data)
    return json_schema