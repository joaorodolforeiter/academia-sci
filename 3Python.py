def main():
    students = []

    while True:

        name = input("Digite o nome do aluno: ")
        grades = []

        for i in range(1, 5):
            grade = float(input(f"digite a {i}. nota: "))
            grades.append(grade)

        students.append(dict(name=name, grades=grades))

        response = get_confirmation()

        if response != "S":
            break

    print_students(students)


def get_confirmation():
    while True:
        response = input("Adicionar mais um estudante? (S/N) ").upper()
        if response == "S" or response == "N":
            return response


def print_students(students):
    print("Alunos registrados:\n")
    for student in students:
        grades_average = sum(student["grades"]) / len(student["grades"])
        if grades_average <= 6:
            status = "REPROVADO"
        else:
            status = "APROVADO"
        print(f"Nome: {student['name']}\n"
              f"Status: {status}\n")


if __name__ == '__main__':
    main()
