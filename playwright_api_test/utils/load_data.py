from pathlib import Path
import json

payload_path = Path(__file__).resolve().parent.parent/"payload_data"


def get_payload_data(payload_file:str):
    payload = payload_path / payload_file
    with open(file=payload, mode="r") as data:
        json_data = json.load(data)
    return json_data