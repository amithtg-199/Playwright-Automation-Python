from jsonschema import validate, ValidationError

def json_schema_validator(json_response:dict,json_scehma:dict):
    try:
        validate(instance=json_response,schema=json_scehma)
        print("[TEST] Schema Validation Sucessfull")
        return True
    except ValidationError as e:
        print(f"[TEST] JSON Schema validation failed with error: {e}")
        return False