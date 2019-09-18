MIN_LENGTH = 6


def main():

    password = get_password(MIN_LENGTH)
    print_stars(password)


def get_password(minimum_length):
    password = input("Enter a password with at least {} characters: ".format(minimum_length))
    while len(password) < MIN_LENGTH:
        print("Password length must be {} or more characters.".format(minimum_length))
        password = input("Enter a password with at least {} characters: ".format(minimum_length))
    return password


def print_stars(password_length):
    print("*" * len(password_length))


main()
