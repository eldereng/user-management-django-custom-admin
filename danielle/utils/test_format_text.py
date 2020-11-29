from utils.format_text import format_text


def test_format_text_returns():
    text = "çAé Líàq "
    result = format_text(text)
    assert result == "CAE LIAQ"
