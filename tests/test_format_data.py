from format_data import format_data_for_display, format_data_for_excel

def test_format_data_for_display(example_people_data):
    result = format_data_for_display(example_people_data)
    assert result == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    result = format_data_for_excel(example_people_data)
    assert result == [
        "given,family,title",
        "Alfonsa,Ruiz,Senior Software Engineer",
        "Sayid,Khan,Project Manager",
    ]