from typing import Dict


def response_structure(data, total_rows: int = None) -> Dict:
    response = {"objects": data}
    if total_rows is not None:
        response["total_rows"] = total_rows
    return response


def error_message(msg: str) -> Dict:
    response = {"error": {"msg": msg}}
    return response
