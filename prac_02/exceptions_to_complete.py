"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


def main():

    finished = False
    result = 0
    while not finished:
        try:
            number = int(input("Please enter a number: "))
            result += number
            finished = True
            pass
        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", result)


main()
