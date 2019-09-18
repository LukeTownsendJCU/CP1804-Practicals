def main():

    name_file = open('name.txt', 'w')
    name = input("Please enter your name: ")
    name_file.write(name)
    name_file.close()

    name_file = open('name.txt', 'r')
    print("Your name is", name_file.read().strip() + ".")
    name_file.close()

    numbers_file = open('numbers.txt', 'r')
    number_one = int(numbers_file.readline())
    number_two = int(numbers_file.readline())
    numbers_file.close()
    result = number_one + number_two
    print(result)


main()
