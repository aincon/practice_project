water = 1000
milk = 1000
coffee = 1000
money = 0.0
tank = ["tank", water, milk, coffee, money]
# 종류, 물, 우유, 커피, 가격
menu = [["espresso", 50, 0, 18, 1.5],
        ["latte", 200, 150, 24, 1.5],
        ["cappuccino", 250, 100, 24, 3.0]]


# return [not enough things, , ...]
def enough(tnk, nam):
    cnt = []
    if tnk[1] < nam[1]:
        cnt.append("water")
    if tnk[2] < nam[2]:
        cnt.append("milk")
    if tnk[3] < nam[3]:
        cnt.append("coffee")
    return cnt


# make coffee
def mk(nam):
    global water
    global milk
    global coffee
    global money
    water -= nam[1]
    milk -= nam[2]
    coffee -= nam[3]
    money += nam[4]
    return


# processing
def setting(tnk, nam):
    if len(enough(tnk, nam)) == 0:
        print(enough(tnk, nam))
        pay = float(input("insert coins:"))
        if pay >= nam[4]:
            mk(nam)
            print(f"Here is ${pay-nam[4]} dollars in change.")
            print(f"Here is your {nam[0]} Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry there is not enough {','.join(enough(tnk, nam))}.")


# notice coffee tank
def Report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


working = True
while working:
    button = input("What would you like? (espresso/latte/cappuccino):")
    if button == "off":
        working = False

    elif button == "report":
        Report()

    for i in menu:
        if button == i[0]:
            setting(tank, i)

