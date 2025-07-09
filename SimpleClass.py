class Simpeclass:
    ...


class Person:
    pass


class Animal:
    var = 2

    def first_method(self):
        print(self.var)


obj_1 = Animal()
obj_2 = Animal()

obj_2.var = 5
obj_1.var = 3
print(obj_1.var)
print(obj_2.var)


class Transport:
    def __init__(self, air, water):
        self.air = air
        self.water = water

    def __str__(self):
        return f"Air: {self.air}, Water: {self.water}"


obj_transport = Transport("airplane", "ship")
print(obj_transport.air, obj_transport.water)


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"Name: {self.fname} {self.lname}")


x = Person(fname="John", lname="Doe")
x.printname()
y = Person(fname="Jane", lname="Doe")
y.printname()


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = [item_name, qty]
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
        else:
            print(f"{item_name} not found.")

    def total_items(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total


cart = ShoppingCart()
cart.add_item("apple", 246)
cart.add_item("banana", 28)
cart.add_item("mango", 3)

print("Current items in cart:")
for item in cart.items:
    print(f"{item[0]}: {item[1]}")

total_qty = cart.total_items()
print(f"Total items in cart: {total_qty}")