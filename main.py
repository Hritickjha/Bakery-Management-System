class Bakery:
    def __init__(self):
        self.menu = {
            "bread": 1.00,
            "croissant": 3.5,
            "muffin": 2.5,
            "cake": 10.0
        }
        self.sales = 0.0

    def display_menu(self):
        print("Bakery Menu")
        for item, price in self.menu.items():
            print(f"{item.capitalize()}: ${price:.2f}")
        print()

    def place_order(self):
        order_total = 0.0
        while True:
            self.display_menu()
            order = input("Enter the item you want to order (or 'done' to finish): ").lower()
            if order == "done":
                break
            if order in self.menu:
                quantity = int(input(f"How many {order}s would you like to order? "))
                order_total += self.menu[order] * quantity
                print(f"Added {quantity} {order}(s) to your order.")
            else:
                print("Sorry, we don't have that item. Please choose from the menu.")
            print()
        
        self.sales += order_total
        print(f"Your order total is ${order_total:.2f}.\nThank you for your order!\n")

    def view_sales(self):
        print(f"Total Sales for the day: ${self.sales:.2f}\n")

def main():
    bakery = Bakery()
    
    while True:
        print("Bakery Management System")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. View Total Sales")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            bakery.display_menu()
        elif choice == "2":
            bakery.place_order()
        elif choice == "3":
            bakery.view_sales()
        elif choice == "4":
            print("Exiting the Bakery Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        print()

if __name__ == "__main__":
    main()

            
    
        
        
                
                   
                    
                   
                 