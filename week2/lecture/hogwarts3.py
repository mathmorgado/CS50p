students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russel terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    }
]

for student in students:
    if student["patronus"] != None:
        print(f"{student["name"]} is from {student["house"]} house and has {student["patronus"]} as patronus.")
    else:
        print(f"{student["name"]} is from {student["house"]} house.")
