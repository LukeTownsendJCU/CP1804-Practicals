from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    silver_taxi.drive(18)
    print("{}({})".format(silver_taxi, silver_taxi.get_fare()))


main()
