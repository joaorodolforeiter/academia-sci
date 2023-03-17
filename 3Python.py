def main():
    students = []

    while True:

        name = input("Digite o nome do aluno: ")
        grades = []

        for i in range(4):
            grade = get_grade(f"Digite a {i + 1}º nota: ")
            grades.append(grade)

        students.append([name, grades])

        response = get_confirmation()

        if response != "S":
            break

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


def get_confirmation():
    while True:
        response = input("Adicionar mais um estudante? (S/N) ").upper()
        if response == "S" or response == "N":
            return response
        else:
            print("Valor invalido, tente novamente:")


def print_students(students):
    print("Alunos registrados:\n")
    for student_name, student_grades in students:
        grades_average = get_grade_average(student_grades)
        if grades_average < 6:
            status = "REPROVADO"
        else:
            status = "APROVADO"
        print(f"Nome: {student_name}\n"
              f"Média: {grades_average}\n"
              f"Status: {status}\n")


if __name__ == '__main__':
    main()
