"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
"""
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""
# TODO: Fix this!


def main():

    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    else:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        elif score < 50:
            print("Bad")


main()
