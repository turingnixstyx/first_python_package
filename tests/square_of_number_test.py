import pytest  # type: ignore # noqa
import random
from sales_transformer.transformer import square_of_number


@pytest.fixture
def random_input_number():
    return random.randint(0, 1000)


def test_square_of_number(random_input_number):
    assert square_of_number(random_input_number) == random_input_number ** 2
