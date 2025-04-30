from typing import Any

def to_bool(value: Any, raise_on_not_match: bool = False) -> bool:
    if isinstance(value, bool):
        value
    
    if not isinstance(value, str):
        value = str(value)

    truthy_values = {'true', '1', 'yes', 'y', 't'}
    falsy_values = {'false', '0', 'no', 'n', 'f'}
    
    string_lower = value.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
    
    if string_lower in truthy_values:
        return True
    elif string_lower in falsy_values:
        return False
    elif raise_on_not_match:
        raise ValueError(f"Cannot convert {value} to a boolean.")
    else:
        return False