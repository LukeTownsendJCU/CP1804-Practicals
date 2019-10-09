from prac_08.unreliable_car import UnreliableCar


def main():

    reliable_car = UnreliableCar("Good Car", 100, 90)
    unreliable_car = UnreliableCar("Bad Car", 100, 9)

    for i in range(1, 14):
        print("Attempting to drive {}km:".format(i))
        print("{} went {}km.".format(reliable_car.name, reliable_car.drive(i)))
        print("{} went {}km. \n".format(unreliable_car.name, unreliable_car.drive(i)))

    print(reliable_car)
    print(unreliable_car)


main()
