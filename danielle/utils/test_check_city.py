from utils.check_city import check_city


def test_check_city_return_true():
    city = "caPitão Poço "
    result = check_city(city)
    assert result


def test_check_city_return_false():
    city = "Fake city"
    result = check_city(city)
    assert not result
