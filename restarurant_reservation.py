def table_reservation():
    amount_of_people = int(input("How many people do you need the table for? "))

    if (amount_of_people >= 8):
        print(f"\nYou will have to wait. We don't have a table for {amount_of_people}.")
    else:
        print("\nYour table is ready, enjoy!")
table_reservation()