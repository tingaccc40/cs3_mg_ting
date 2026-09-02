class Pizza:
    def __init__(self,topping1,topping2,topping3):
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3
        self.toppingprice = 1.50
        self.baseprice = 10.00
        self.toppingcount = 3
        

    def calculatetotal(self):
        return (self.toppingcount * self.toppingprice) + self.baseprice
    
Pizza_Toppings = ["Pepperoni", "Mushrooms", "Extra_Cheese"]

print("Hi !! Welcome to the Online PSHS Pizza Parlor. Please choose exactly 3 toppings!")
print("Options: Pepperoni, Mushrooms, Extra_Cheese")


while True:
    topping1 = input("Enter topping 1: ")
    if topping1 in Pizza_Toppings:
        break
    print("Error!! Not in menu, check for typos!")


while True:
    topping2 = input("Enter topping 2: ")
    if topping2 in Pizza_Toppings:
        break
    print("Error!! Not in menu, check for typos!")


while True:
    topping3 = input("Enter topping 3: ")
    if topping3 in Pizza_Toppings:
        break
    print("Error!! Not in menu, check for typos!")


pizza1 = Pizza(topping1, topping2, topping3)


print(f"Your toppings: {pizza1.topping1}, {pizza1.topping2}, {pizza1.topping3}")
print(f"Your total bill is: ${pizza1.calculatetotal()}")


