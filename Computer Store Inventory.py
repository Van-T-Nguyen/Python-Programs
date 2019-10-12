#Van Nguyen
#3/15/2018
# This program prints store inventory data in a clean format
#You will create a program that will take comma delimited input for the inventory
#  of a small computer store. Information stored in the comma delimited file include the product name,
#  of items on hand, and wholesale cost. Extend the value of each item and provide the total value of the
#  inventory. A file with input and expected output is attached.
#Make sure you strip all leading and following spaces. Use conversion specifiers, flags and field width specifiers as needed.
#Use internal documentation, good prompts to the user, and meaningful variable

def main():
    print("This program prints store inventory data in a clean format.")
    data = input("Please enter the store data: ")
    store_data = data.split(",")
    inventory = []
    for items in store_data:
        inventory.append(items.strip())
    print(inventory)

    total = 0
    for x in range(len(inventory))[0::3]:
        sum = (int(inventory[x+1]) * float(inventory[x+2]))
        total = total + sum
        print("%-20s %-10.2f $%-10.2f $%-10.2f"
              % (inventory[x], float(inventory[x + 1]), float(inventory[x + 2]), sum))
    print("The total value of the inventory is $%.2f." % total)

main()



