from utils.format_text import format_text
from .all_valid_brasilian_cities_list import cities
from django.core.exceptions import ValidationError


def check_city(city):
    city = format_text(city)
    formatted_cities = [format_text(c) for c in cities]
    if city not in formatted_cities:
        raise ValidationError("Cidade não encontrada.")
