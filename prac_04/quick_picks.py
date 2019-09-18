import random

NUMBERS_EACH_PICK = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_picks = int(input("Number of quick picks: "))
    while number_of_picks < 0:
        print("Number of picks must be 1 or more.")
        number_of_picks = int(input("Number of quick picks: "))

    for pick in range(number_of_picks):
        quick_picks = []
        for number in range(NUMBERS_EACH_PICK):
            pick_number = random.randint(MINIMUM, MAXIMUM)
            while pick_number in quick_picks:
                pick_number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(pick_number)
        quick_picks.sort()
        # print(quick_picks)
        print(" ".join("{:2}".format(number) for number in quick_picks))


main()
