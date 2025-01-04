def add_item(cart):
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item} (in rupees): "))
    quantity = int(input(f"Enter quantity of {item}: "))
    cart.append((item, price, quantity))

def display_bill(cart):
    print("\n____________ Your Bill ____________")
    total = 0
    for item, price, quantity in cart:
        total += price * quantity
        print(f"{item} * {quantity} = ₹{price * quantity:.2f}")
    print(f"Total Bill: ₹{total:.2f}\n")

def grocery_store():
    cart = []
    while True:
        choice = input("1. Add item\n2. View bill\n3. Exit\nEnter your choice (1-3): ")
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            display_bill(cart)
        elif choice == "3":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the grocery store
grocery_store()
