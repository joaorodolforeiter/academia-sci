def main():
    students = []
    for i in range(3):
        student_name = input(f"Digite o nome do {i + 1}º estudante: ")
        grades = []
        for j in range(4):
            grade = get_grade(f"Digite a {j + 1}º nota: ")
            grades.append(grade)
        grade_average = get_grade_average(grades)
        students.append([student_name, grade_average])

    print_students(students)


def get_grade(prompt):
    while True:
        grade = float(input(prompt))
        if 0 <= grade <= 10:
            return grade
        else:
            print("Nota invalida, tente novamente:")


def get_grade_average(grades):
    average = sum(grades) / len(grades)
    return average


def print_students(students):
    bigger_average = students[0]
    smaller_average = students[0]

    print("Médias: ")
    for student, average in students:
        if average > bigger_average[1]:
            bigger_average = student, average
        if average < smaller_average[1]:
            smaller_average = student, average
        print(f"{student}: {average}")

    print(f"Menor média: {smaller_average[0]}, {smaller_average[1]}")
    print(f"Maior média: {bigger_average[0]}, {bigger_average[1]}")


if __name__ == '__main__':
    main()
