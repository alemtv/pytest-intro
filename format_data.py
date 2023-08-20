people = [
    {
        "given_name": "Alfonsa",
        "family_name": "Ruiz",
        "title": "Senior Software Engineer",
    },
    {
        "given_name": "Sayid",
        "family_name": "Khan",
        "title": "Project Manager",
    },
]

def format_data_for_display(people):
    return [f"{person['given_name']} {person['family_name']}: {person['title']}" for person in people]

def format_data_for_excel(people):
    header = "given,family,title"
    data = [f"{person['given_name']},{person['family_name']},{person['title']}" for person in people]
    return [header ] + data

if __name__ == "__main__":
    format_data_for_excel(people)