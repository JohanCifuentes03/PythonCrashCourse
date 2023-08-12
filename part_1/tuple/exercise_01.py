foods = ("pizza", "meat", "rice", "sup")
# foods[1] = "hot dog" -- I can't reassign values in a tuple. I have to rewrite

foods = ("pizza", "hot dog", "Burger", "sup")
print("Menu: ")
i = 0
for food in foods:
    print(f"\t({i}) {food.title()}")
    i = i + 1
foodsOrder = []

condition = True
while condition:
    option = int(input("What do you want? (-1 to exit): "))

    if option == -1:
        condition = False
    else:
        foodsOrder.append(foods[option])

print("Your order is: ")
for food in foodsOrder:
    print(food)