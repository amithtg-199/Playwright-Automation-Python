import pandas as pd
import json
from openpyxl import load_workbook
from pathlib import Path
import logging

log = logging.getLogger(__name__)


##########################################
# Test Data Path to be sent in Test cases
##########################################
# TEST_DATA_PATH = Path(__file__).resolve().parent.parent/"testdata"
# JSON_FILE = TEST_DATA_PATH / "logindata.json"
# CSV_FILE = TEST_DATA_PATH / "logindata.csv"
# XLS_FILE = TEST_DATA_PATH / "logindata.xlsx"


##########################################
# Import Data from JSON
##########################################
def get_test_data_json(json_data_path:str):
    json_test_data = []
    with open(json_data_path) as f:
        json_data = json.load(f)
        for data in json_data:
            json_test_data.append((tuple(data.values())))
    log.info(f"Extracted test data from JSON {json_data_path}")
    return json_test_data

##########################################
# Import Data from CSV
##########################################
def get_test_data_csv(csv_data_path:str):
    df = pd.read_csv(csv_data_path)
    csv_test_data = [tuple(row) for row in df.itertuples(index=False)]
    log.info(f"Extracted test data from CSV {csv_data_path}")
    return csv_test_data

##########################################
# Import Data from XLS (Here minrow=2 because to skip the column headers, minrow starts from 1)
##########################################
def get_test_data_xls(xls_data_path:str):
    workbook = load_workbook(xls_data_path, data_only=True)
    worksheet = workbook.active
    data = list(
        tuple(row)
        for row in worksheet.iter_rows(values_only=True, min_row=2)
    )
    workbook.close()
    log.info(f"Extracted test data from CSV {xls_data_path}")
    return data