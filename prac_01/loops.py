def main():

    for i in range(1, 21, 2):
        print(i)
    for i in range(0, 101, 10):
        print(i)
    for i in range(20, 0, -1):
        print(i)

    number_of_stars = int(input("Enter Number: "))
    for i in range(number_of_stars):
        print("*", end=' ')
    for i in range(1, number_of_stars + 1):
        print("*" * i)


main()
