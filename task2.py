import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b|\b\d+\b'
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

