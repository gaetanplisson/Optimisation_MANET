from functools import *
from typing import *
from itertools import *
from collections import defaultdict
def generic(obj):
    def check(key, value):
        if 'registered_types' not in value.__dict__:
            raise AttributeError(f"{value} is not a generic type")
        if type(key) not in value.registered_types:
            raise TypeError(f"Expected {value.registered_types}, got {type(key)}")

    grouped_obj = defaultdict(list)
    for key, value in obj.items():
        grouped_obj[key].append(value)

    for key, values in grouped_obj.items():
        for value in values:
            check(key, value)