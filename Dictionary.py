students = {
    "name" : "Viral Trivedi",
    "subjects": {
        "Phy": 89,
        "Maths":93, 
    }
}

print(students["name"])
print(students["subjects"]["Maths"])

print(students.keys())
print(students.values())
print(students.items())
print(students.get("subjects"))

new_dict = {
    "Age": 23,
    "City": "Kitchener"
}

students.update(new_dict)

print(students)