from prac_08.taxi import Taxi


# Classes don't ever use def main?


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        # Does it matter what order these are in.
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "${} flagfall and taxi fare for {}".format(self.flagfall, super().__str__())

    def get_fare(self):
        # Are we doing the maths in the return because its not a variable we need to keep track of?
        return self.flagfall + super().get_fare()
