import pytest

from dcs_split_by_first_line.types import SplitTextByFirstLine

pytestmark = [pytest.mark.django_db(transaction=True)]


@pytest.mark.parametrize(
    "var,value",
    [
        (
            SplitTextByFirstLine(split_default_key="BEST"),
            "string",
        ),
    ],
)
def test_value(var, value):
    assert var.get_help() == value

