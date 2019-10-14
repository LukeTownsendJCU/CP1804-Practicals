"""Client code"""
from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2012, 66.6)
    print("{} get_age() - Expected {}. Got {}.".format(guitar.name, 97, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}.".format(another.name, 7, another.get_age()))
    print("{} get_age() - Expected {}. Got {}.".format(guitar.name, True, guitar.is_vintage()))
    print("{} get_age() - Expected {}. Got {}.".format(another.name, False, another.is_vintage()))


main()
