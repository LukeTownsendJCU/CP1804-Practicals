from prac_06.guitar import Guitar


def main():
    guitars = []

    print("Your guitars!")
    guitar_name = input("Enter a blank name to quit.\nEnter name of guitar: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        added_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(added_guitar)

        print(added_guitar, "added.\n"
                            "Add another guitar?")
        guitar_name = input("Enter name of guitar: ")

    # For testing.
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # Found this very useful: lists, strings and other collections are False when empty, True when non-empty

    # If statement is to check if any guitars were entered.
    if guitars:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))
            # First {} is for the index.
            # The second one prints the guitar name right to left from 20 spaces.
            # And the third prints the cost right to left from 10 spaces.
            # And the final {} prints vintage_string if it's True.

            # print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
            # {2}".format(i + 1, guitar, vintage_string))
    else:
        print("Have a good day.")


main()
