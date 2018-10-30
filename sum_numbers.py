import sys


def sum_numbers_multiple(num):
    numbers = []
    for i in range(num):
        if i % 3 == 0:
            numbers.append(i)
        elif i % 5 == 0:
            numbers.append(i)
    return sum(numbers)


def menu():
    number = input('Type a number or "X" to exit: ')
    if number.lower() == 'x':
        sys.exit(0)
    try:
        int(number)
    except ValueError:
        print('Invalid number. Try again.')
        menu()

    print('The sum of all multiples of 3 or 5 is: "{}"'.format(sum_numbers_multiple(int(number))))
    menu()


if __name__ == '__main__':
    menu()

