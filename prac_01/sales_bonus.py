"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():

    users_sales = float(input("Please enter sales: $"))
    while users_sales >= 0:
        if users_sales < 1000:
            bonus = users_sales * 0.1
        else:
            bonus = users_sales * 0.15
        print("{:.2f}".format(bonus))
        users_sales = float(input("Please enter sales: $"))


main()
