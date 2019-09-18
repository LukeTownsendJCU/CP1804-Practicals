def main():

    total_price_of_items = 0
    number_of_items = int(input("Please enter the number of items you are purchasing: "))
    while number_of_items <= 0:
        print("Invalid amount.")
        number_of_items = int(input("Please enter the number of items you are purchasing: "))
    for i in range(number_of_items):
        price_of_item = float(input("Price of item: "))
        total_price_of_items += price_of_item
    if total_price_of_items > 100:
        discount = total_price_of_items * 0.1
        total_price_of_items = total_price_of_items - discount
    print("Number of items:", number_of_items)
    for i in range(number_of_items):
        print("Price of item: ", "{:.2f}".format(price_of_item))
    print("Total price for", number_of_items, "is", "{:.2f}".format(total_price_of_items))


main()
