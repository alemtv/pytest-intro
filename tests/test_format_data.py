import pytest
from format_data import format_data_for_display, format_data_for_excel

@pytest.mark.format_data
def test_format_data_for_display(example_people_data):
    result = format_data_for_display(example_people_data)
    assert result == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

@pytest.mark.format_data
def test_format_data_for_excel(example_people_data):
    result = format_data_for_excel(example_people_data)
    assert result == [
        "given,family,title",
        "Alfonsa,Ruiz,Senior Software Engineer",
        "Sayid,Khan,Project Manager",
    ]