from collections import OrderedDict
import re

camel_case_regex = re.compile(r"(?<=[a-z0-9])_[a-z0-9]")
underscore_regex = re.compile(r"(?<=[a-zA-Z0-9])([A-Z0-9])")

def convert_to_camel_case(data):
    if isinstance(data, list):
        return [convert_to_camel_case(x) for x in data]

    if isinstance(data, tuple):
        return tuple(convert_to_camel_case(x) for x in data)

    if isinstance(data, dict):
        transformed_data = {}
        for underscore_key, value in data.items():
            camel_case_key = camel_case_regex.sub(lambda x: x.group()[1].upper(), underscore_key)
            transformed_data[camel_case_key] = convert_to_camel_case(value)
        return transformed_data

    return data

def convert_to_underscore(data):
    if isinstance(data, list):
        return [convert_to_underscore(x) for x in data]

    if isinstance(data, tuple):
        return tuple(convert_to_underscore(x) for x in data)

    if isinstance(data, dict):
        transformed_data = {}
        for camel_case_key, value in data.items():
            underscore_key = underscore_regex.sub(r"_\1", camel_case_key).lower()
            transformed_data[underscore_key] = convert_to_underscore(value)
        return transformed_data

    return data