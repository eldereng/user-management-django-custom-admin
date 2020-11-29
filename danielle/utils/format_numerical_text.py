import re


def format_numerical_text(numerical_text):
    pattern = re.compile(r"[^0-9]+")
    return re.sub(pattern, '', numerical_text)
