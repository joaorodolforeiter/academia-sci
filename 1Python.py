def main():
    numbers = []

    for i in range(1, 6):
        number = int(input(f"Digite o {i}. número: "))
        numbers.append(number)

    even_numbers = list(filter(is_even, numbers))
    odd_numbers = list(filter(is_odd, numbers))
    mean = sum(numbers) / len(numbers)

    print("Números pares:\n"
          f"{even_numbers}")
    print("Números impares:\n"
          f"{odd_numbers}")
    print("Média:\n"
          f"{mean}")


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return not (num % 2 == 0)


if __name__ == '__main__':
    main()
