#Van Nguyen
#4/10/2018
#Assignment 1

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

    while name != "":
        zone = input("Please enter a the zone number between 1 - 3: ")
        num = input("Please enter the number of packages: ")
        cost = pack(zone) * float(num)
        print("The cost of your shipping is $%.2f" % cost)
        name = input("Please enter your name: ")
    print("Thank you for your patronage")


main()