# Restaurant Management System Using Functions

menu = {
    "Chicken Biryani": 280.0,
    "Mutton Biryani": 350.0,
    "Veg Biryani": 220.0,
    "Pizza": 250.0,
    "Burger": 150.0,
    "Pasta": 200.0,
    "Sandwich": 120.0,
    "French Fries": 100.0,
    "Chicken Fried Rice": 180.0,
    "Veg Fried Rice": 160.0,
    "Chicken Noodles": 190.0,
    "Veg Noodles": 170.0,
    "Butter Chicken": 260.0,
    "Paneer Butter Masala": 220.0,
    "Chicken Curry": 240.0,
    "Dal Fry": 140.0,
    "Roti": 20.0,
    "Naan": 35.0,
    "Ice Cream": 90.0,
    "Cold Drink": 50.0,
    "Coffee": 80.0,
    "Tea": 30.0
}

# Add Food Item
def add_item():
    item = input("Enter Food Item Name: ")

    if item in menu:
        print("Food Item Already Exists!")
        return

    price = float(input("Enter Price: "))
    menu[item] = price
    print("Food Item Added Successfully!")

# View Menu
def view_menu():
    print("\n==================== MENU ====================")
    print("{:<5}{:<25}{:<10}".format("No.", "Food Item", "Price"))
    print("-" * 45)

    count = 1
    for item, price in menu.items():
        print("{:<5}{:<25}₹{:<10.2f}".format(count, item, price))
        count += 1

    print("-" * 45)
    print("Total Food Items:", len(menu))

# Update Food Item
def update_item():
    item = input("Enter Food Item Name to Update: ")

    if item in menu:
        new_price = float(input("Enter New Price: "))
        menu[item] = new_price
        print("Price Updated Successfully!")
    else:
        print("Food Item Not Found!")

# Delete Food Item
def delete_item():
    item = input("Enter Food Item Name to Delete: ")

    if item in menu:
        confirm = input("Are you sure you want to delete? (y/n): ")

        if confirm.lower() == "y":
            del menu[item]
            print("Food Item Deleted Successfully!")
        else:
            print("Deletion Cancelled.")
    else:
        print("Food Item Not Found!")

# Search Food Item
def search_item():
    item = input("Enter Food Item Name to Search: ").lower()

    for food, price in menu.items():
        if food.lower() == item:
            print(f"{food} : ₹{price:.2f}")
            return

    print("Food Item Not Found!")

# Order Food and Generate Bill
def order_food():
    total = 0
    bill = []

    print("\n========== ORDER FOOD ==========")

    while True:
        item = input("Enter Food Item (or type 'done' to finish): ")

        if item.lower() == "done":
            break

        if item in menu:
            qty = int(input("Enter Quantity: "))
            amount = menu[item] * qty
            total += amount
            bill.append([item, menu[item], qty, amount])
            print(item, "added successfully!")
        else:
            print("Food Item Not Found!")

    if len(bill) == 0:
        print("No items ordered.")
        return

    print("\n============== RESTAURANT BILL ==============")
    print("{:<25}{:<10}{:<8}{:<10}".format("Item", "Price", "Qty", "Amount"))
    print("-" * 55)

    for item, price, qty, amount in bill:
        print("{:<25}₹{:<9.2f}{:<8}₹{:<10.2f}".format(item, price, qty, amount))

    print("-" * 55)
    print(f"Total Bill: ₹{total:.2f}")
    print("=============================================")
    print("Thank You! Visit Again 😊")

# Main Function
def main():
    while True:
        print("\n" + "=" * 50)
        print("      RESTAURANT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Food Item")
        print("2. View Menu")
        print("3. Update Food Item")
        print("4. Delete Food Item")
        print("5. Search Food Item")
        print("6. Order Food & Calculate Bill")
        print("7. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_menu()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            search_item()
        elif choice == "6":
            order_food()
        elif choice == "7":
            print("\nThank You for Using Restaurant Management System!")
            print("Have a Nice Day 😊")
            break
        else:
            print("Invalid Choice! Please Try Again.")

# Run Program
main()