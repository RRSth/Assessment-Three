def calculate(item_list, item_idx):
    item_price = float(item_list[item_idx + 1])
    item_amount = int(input(f"How many {item_list[item_idx]} do you want: "))
    return item_price * item_amount


fruit = ["banana", 2.00, "avocado", 1.50, "oranges", 1.50, "apples", 2.00, "kiwi", 1.50]
veges = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad mix", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

cartprice = 0
cartitems = []

while True:
    print("Select Area to Shop")
    print("(F)ruit")
    print("(V)egetables")
    print("(D)elicatessan")
    print("E(x)it")
    area = input("Enter letter of area to shop: ").lower()

    if len(area) > 1:
        area = area[0]

    if area == "f":
        print("(A)pples")
        print("A(v)ocado")
        print("(B)anana")
        print("(K)iwifruit")
        print("(O)ranges")
        print("(G)o Back")
        fruit_choice = input("Enter Fruit letter: ").lower()

        if len(fruit_choice) > 1:
            fruit_choice = fruit_choice[0]

        choices = ["a", "v", "b", "k", "o", "g"]

        
        if fruit_choice not in choices:
            print("Selection Error")
            continue
        elif fruit_choice == "a":
            fruit_find =  fruit.index("apples")
        elif fruit_choice == "v":
            fruit_find =  fruit.index("avocado")
        elif fruit_choice == "b":
            fruit_find =  fruit.index("banana")
        elif fruit_choice == "k":
            fruit_find =  fruit.index("kiwi")
        elif fruit_choice == "o":
            fruit_find =  fruit.index("oranges")
        else:
            continue
		
        """
        match fruit_choice:
            case "a":
                fruit_find = fruit.index("apples")
            case "v":
                fruit_find = fruit.index("avocado")
            case "b":
                fruit_find = fruit.index("banana")
            case "k":
                fruit_find = fruit.index("kiwi")
            case "0":
                fruit_find = fruit.index("oranges")
            case _:
                continue
		"""
        fruit_cost = calculate(fruit, fruit_find)
        cartprice += fruit_cost
        cartitems.append(fruit[fruit_find])

    # students to complete the other 2 elif statements

    else:
        print("Thank you for shopping with us")
        currency = "${:,.2f}".format(cartprice)
        print(f"\nTotal cost = {currency}")
        print(f"The items selected where: {cartitems}")
        break

    currency = "${:,.2f}".format(cartprice)
    print(f"\nCost so far = {currency}")
    print(f"Cart items = {cartitems}\n")
