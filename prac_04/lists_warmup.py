"""Change the first element of numbers to "ten"
Change the last element of numbers to 1
Get all the elements from numbers except the first two
Check if 9 is an element of numbers"""


def main():

    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(numbers)
    numbers[0] = "ten"
    print(numbers)
    numbers[-1] = 1
    print(numbers)
    print(numbers[2:])


main()
