def main():
    numbers = []

    for i in range(1, 6):
        number = int(input(f"Digite o {i}. número: "))
        numbers.append(number)

    print(f"Maior número: {min(numbers)}")
    print(f"Menor número: {max(numbers)}")


if __name__ == '__main__':
    main()
