import pytest

from dcs_split_by_first_line.types import SplitByFirstLine


pytestmark = [pytest.mark.django_db(transaction=True)]


@pytest.mark.parametrize(
    "input_text, expected_text",
    [
        pytest.param("Text", "<pre>Text</pre>", id="text"),
        pytest.param("""
===EN===
Text
===UA===
Текст
         """.strip(), '<div> <b>EN</b>  <a class="cs_set_params" data-param-suffix="UA">UA</a> </div><pre>Text</pre>', id="en_ua"),
    ],
)
def test_admin_preview(input_text, expected_text):
    VAR = SplitByFirstLine(split_default_key="EN")
    assert VAR.get_admin_preview_value(input_text, "VAR") == expected_text
