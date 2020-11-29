from utils.format_text import format_text
from .all_valid_brasilian_cities_list import cities


def check_city(city):
    city = format_text(city)
    formatted_cities = [format_text(c) for c in cities]
    return city in formatted_cities
