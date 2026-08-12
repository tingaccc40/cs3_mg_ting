Cheese_Pizza = 10.00
Pepperoni = 1.50
Mushrooms = 1.50
Extra_Cheese = 1.50

print("Hi !! Welcome to the Online PSHS Pizza Parlor. Feel free to choose any amount of toppings from our available options!")
print("Pepperoni, Mushrooms, Extra Cheese")

def calculate_total(topping_count):
    topping_count = input(("Enter topping name: (Done to finish order)"))
    while topping_count != "Done":
        