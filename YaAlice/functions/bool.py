def from_json_bool_to_py_bool(value: str | bool) -> bool | int:
    if isinstance(value, str):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        else:
            return -1
    elif isinstance(value, bool):
        return value
    else:
        return -1