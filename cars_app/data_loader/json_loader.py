from typing import Any
import json


def get_cars_data(filename: str) -> list[dict[str, Any]]:
    with open(filename, 'r') as jf:
        return json.load(jf)