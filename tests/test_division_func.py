from utils import division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (10, 1, 10),
                                                   (10, 10, 1),
                                                   (10, -1, -10)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("div, divider, expected_exception",
                         [(10, 0, ZeroDivisionError),
                            (10, "10", TypeError)])
def test_division_with_error(div, divider, expected_exception):
    with pytest.raises(expected_exception):
        assert division(div, divider) == expected_exception