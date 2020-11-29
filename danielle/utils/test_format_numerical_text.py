from utils.format_numerical_text import format_numerical_text


def test_utils_format_numerical_text_returns():
    text = "  12 3a3.2 "
    result = format_numerical_text(text)
    assert result == '12332'


def test_utils_format_numerical_text_with_zero_in_start():
    text = '047a'
    result = format_numerical_text(text)
    assert result == "047"
