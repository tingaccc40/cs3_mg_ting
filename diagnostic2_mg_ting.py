Pizza_Toppings = ["Pepperoni", "Mushrooms", "Extra_Cheese"]
Cheese_Pizza = 10.00

print("Hi !! Welcome to the Online PSHS Pizza Parlor. Feel free to choose any amount of toppings from our available options!")
print("Pepperoni, Mushrooms, Extra Cheese")

def calculate_total(topping_count):
    cheese_pizza = 10.00
    toppings = 1.50
    return (topping_count * 1.50) + Cheese_Pizza

topping_count = 0


while True:
    toppingselection = input(("Enter topping name, (Done if you want to finish the order):"))

    if toppingselection in Pizza_Toppings:
        topping_count += 1
    elif toppingselection == "Done":
        break
    else:
        print("Error!! Not in menu, please check for typos!")

    total_bill = calculate_total(topping_count)
print(f"Your total bill is: {total_bill}")