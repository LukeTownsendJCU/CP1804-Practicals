def main():
    """Note that you can use the functions min, max, sum and len,
    and you can use the append method to add a number to a list."""
    user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                  'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                  'bob']
    user_name_check = input("Please enter user name: ")
    if user_name_check in user_names:
        print("Access Granted.")
    else:
        print("Access denied.")

    numbers = []
    first_number = int(input("Number: "))
    numbers.append(first_number)
    second_number = int(input("Number: "))
    numbers.append(second_number)
    third_number = int(input("Number: "))
    numbers.append(third_number)
    fourth_number = int(input("Number: "))
    numbers.append(fourth_number)
    fifth_number = int(input("Number: "))
    numbers.append(fifth_number)

    print("The first number is {}.".format(numbers[0]))
    print("The last number is {}.".format(numbers[-1]))
    print("The smallest number is {}.".format(min(numbers)))
    print("The largest number is {}.".format(max(numbers)))
    print("The average of these numbers is {}.".format(sum(numbers) / (len(numbers))))


main()
