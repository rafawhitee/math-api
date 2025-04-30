from typing import Any

def get_value_or_none(map: dict, key: str) -> Any:
   return get_value_or_default(map, key, None)

def get_value_or_default(map: dict, key: str, default_value: Any) -> Any:
    if not isinstance(map, dict) or key == None:
        return default_value
    if key in map:
        return map[key]
    return default_value