# This loop will go on until the budget is integer or float
while True:
    try:
        bg = float(input("Enter your budget: "))
        # if budget is integer or float it will be stored
        # temporarily in variables
        s = bg
    except ValueError:
        print("PRINT NUMBER AS A AMOUNT")
        continue
    else:
        break

# dictionary to store product("name"), quantity("quant")
# price("price") with empty list as their values
a = {"name": [], "quant": [], "price": []}

# This loop terminates when user selects 2.EXIT option when asked
# in try it will ask user for an option as an integer (1 or 2)
# if correct then proceed else continue asking options
while True:
    try:
        ch = int(input("1.ADD\n2.EXIT\nEnter your choice: "))
    except ValueError:
        print("\nERROR: Choose only digits from the given option")
        continue
    else:
        # check if the budget is greater than zero and option selected
        # by user is 1 i.e. to add an item
        if ch == 1 and s > 0:
            # input products name
            pn = input("Enter product name: ")
            # input quantity of product
            q = int(input("Enter quantity: "))
            # input price of the product
            p = float(input("Enter price of the product: "))

            if p > s:
                # checks if product name already in list
                print("\nCAN'T BUY THE PRODUCT")
                continue
            else:
                # checks if product name already in list
                if pn in a["name"]:
                    # find the index of that product
                    ind = a["name"].index(pn)
                    # remove quantity from "quant" index of the product
                    a["quant"][ind] = q
                    # remove price from "price" index of the product
                    a["price"][ind] = p
                    # subtracting the price from the budget and assign
                    # it to s
                    s = bg - sum(a["price"])

                    print("\namount left", s)
                else:
                    # append value of in "name","quantity", "price"
                    a["name"].append(pn)
                    # append quantity and price
                    a["quant"].append(q)
                    a["price"].append(p)
                    # after appending new value the sum in price
                    # as to be calculated
                    s = bg - sum(a["price"])
                    print("\namount left", s)
        # if budget goes zero print "NO BUDGET"
        elif s <= 0:
            print("\nNO BUDGET")
        else:
            break

# will print amount left in variable 's'
print("\nAmount left: Rs.", s)
# if the amount left equals to any amount in price list
if s in a["price"]:
    # then printing the name of the amount in price list
    print("\nAmount left can buy you a", a["name"][a["price"].index(s)])

print("\n\n\nGROCERY LIST")
# print final grocery list
for i in range(len(a["name"])):
    print(a["name"][i], a["quant"][i], a["price"][i])