from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

"""Write a taxi simulator program that uses your Taxi and SilverServiceTaxi
    classes. Each time, until they quit:
    The user should be presented with a list of available taxis and get to
    choose one. Then they should say how far they want to drive.
    At the end of each trip, show them the price and add it to their bill.
    """


def main():
    total_fare_cost = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu_choice = input("(C)hoose Taxi, (D)rive, (Q)uit Program").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Available Taxis:")
            taxis_display(taxis)
            taxi_choice = int(input("Choose taxi by its number: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_of_drive = float(input("How far would you like to go?\nPlease enter numerical value:"))
            current_taxi.drive(distance_of_drive)
            fare_cost = current_taxi.get_fare()
            print("Your {} fare will cost you {:.2f}.".format(current_taxi.name, fare_cost))
            total_fare_cost += fare_cost

        else:
            print("Invalid menu option.")
            print("Current bill = {:.2f}.".format(total_fare_cost))
            menu_choice = input("(C)hoose Taxi, (D)rive, (Q)uit Program").lower()

    print("Total cost of your trip is {:.2f}.")
    print("The taxis are now:")
    taxis_display(taxis)


def taxis_display(taxis):
    for i, taxi in enumerate(taxis):
        print("{:5} - {}.".format(i, taxi))


main()
