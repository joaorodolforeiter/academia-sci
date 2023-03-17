numbers = [[], []]


def main():
    for i in range(1, 6):
        number = float(input(f"Digite o {i}. número: "))
        numbers.append(number)
    print(f"Terceiro número: {numbers[2]}")


if __name__ == '__main__':
    main()
