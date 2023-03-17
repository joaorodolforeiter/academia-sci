def main():
    numbers = []
    for i in range(5):
        number = float(input(f"Digite o {i + 1}º número: "))
        numbers.append(number)
    print(f"Terceiro número: {numbers[2]}")


if __name__ == '__main__':
    main()
