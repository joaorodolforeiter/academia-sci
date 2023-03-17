def main():
    numbers = []

    for i in range(5):
        number = int(input(f"Digite o {i+1}º número: "))
        numbers.append(number)

    even_numbers = list(filter(is_even, numbers))
    odd_numbers = list(filter(is_odd, numbers))
    average = sum(numbers) / len(numbers)

    print(f"Números pares: {even_numbers}")
    print(f"Números impares: {odd_numbers}")
    print(f"Média: {average}")


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


if __name__ == '__main__':
    main()
