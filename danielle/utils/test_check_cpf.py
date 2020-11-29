from utils.check_cpf import check_cpf


def test_check_cpf_returns_true_to_valid_cpf():
    cpf = '670.510a600-07'
    result = check_cpf(cpf)
    assert result


def test_check_cpf_returns_false_to_invalid_cpf():
    cpf = '670.530a600-07'
    result = check_cpf(cpf)
    assert not result
