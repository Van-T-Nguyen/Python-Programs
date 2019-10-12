def pack(zone):
    if zone == 1:
            ship = .50
    elif zone == 2:
            ship = 1.00
    else:
            ship = 1.50

    return ship

def main():
    name = input("Please enter your name: ")

    zone = input("Please enter a the zone number between 1 - 3: ")
    num = input("Please enter the number of packages: ")
    cost = pack(zone) * float(num)
    print("The cost of your shipping is $%.2f" % cost)

    txt = open("shippingCosts.txt", "w")
    file = (name,
                num,
                zone,
                pack(zone))
    txt.append(file)
    print(txt)

main()