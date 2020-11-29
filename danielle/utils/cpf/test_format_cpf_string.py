from utils.cpf.format_cpf_string import format_cpf_string


def test_format_cpf_string_return():
    cpf = "00000000000"
    result = format_cpf_string(cpf)
    assert result == "000.000.000-00"
