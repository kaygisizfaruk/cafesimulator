class Cafe:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append({"item": item.name, "price": item.price})

    def display_menu(self):
        print(f"\nMenu for {self.name}")
        for item in self.menu:
            print(f"{item['item']}: £{item['price']}")
        print("\n")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.items = []
        self.total_price = 0
    
    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def display_order(self):
        print(f"\nOrder number: {self.order_number}")
        for item in self.items:
            print(f"Item: {item.name}, Price: {item.price}")
        print(f"Total Price: {self.total_price}")

cafe = Cafe("Cosy Cafe")

item1 = Item("Coffee", 3)
item2 = Item("Tea", 2)
item3 = Item("Hot Chocolate", 3)
item4 = Item("Croissant", 3)
item5 = Item("Sandwich", 5)
item6 = Item("Doughnut", 2)

cafe.add_menu_item(item1)
cafe.add_menu_item(item2)
cafe.add_menu_item(item3)
cafe.add_menu_item(item4)
cafe.add_menu_item(item5)
cafe.add_menu_item(item6)

def order_item():
    cafe.display_menu()
    choice = input("\nPlease enter the name of the item you would like to order: ")
    order = Order(1)
    if choice == "Coffee":
        order.add_item(item1)
        order.display_order()
    elif choice == "Tea":
        order.add_item(item2)
        order.display_order()
    elif choice == "Hot Chocolate":
        order.add_item(item3)
        order.display_order()
    elif choice == "Croissant":
        order.add_item(item4)
        order.display_order()
    elif choice == "Sandwich":
        order.add_item(item5)
        order.display_order()
    elif choice == "Doughnut":
        order.add_item(item6)
        order.display_order()
    else:
        print("\nSorry, that item is not on the menu.")
        order_item()

def run():
    while True:
        print("Welcome to the Cosy Cafe!")
        print("What can we get for you today?")
        order_item()
        break
        

run()



