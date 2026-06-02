import json


gradebook = {}


def add_grade(student, grade):

    if grade < 0 or grade > 100:
        print("Invalid Grade")
        return

    if student not in gradebook:
        gradebook[student] = []

    gradebook[student].append(grade)


def calculate_gpa(student):

    if student not in gradebook:
        return 0

    grades = gradebook[student]

    return sum(grades) / len(grades)


def save_data():

    with open("grades.json", "w") as file:
        json.dump(gradebook, file, indent=4)

    print("Grades Saved")


def load_data():

    global gradebook

    try:
        with open("grades.json", "r") as file:
            gradebook = json.load(file)

        print("Grades Loaded")

    except FileNotFoundError:
        print("File Not Found")


def class_average():

    total = 0
    count = 0

    for grades in gradebook.values():
        total += sum(grades)
        count += len(grades)

    if count == 0:
        return 0

    return total / count


add_grade("Hari", 85)
add_grade("Hari", 90)

add_grade("Femilin", 75)
add_grade("Femilin", 80)

save_data()

load_data()

print(f"Hari GPA: {calculate_gpa('Hari'):.2f}")
print(f"Rahul GPA: {calculate_gpa('Femilin'):.2f}")

print(f"Class Average: {class_average():.2f}")