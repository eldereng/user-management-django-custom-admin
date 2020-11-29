import re
from utils.format_numerical_text import format_numerical_text


def format_cpf_string(cpf: str) -> str:
    cpf = format_numerical_text(cpf)
    pattern = re.compile(r'(\d{3})(\d{3})(\d{3})(\d{2})')
    return re.sub(pattern, r'\g<1>.\g<2>.\g<3>-\g<4>', cpf)
