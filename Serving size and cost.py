#Van Nguyen
#3/8/2018
#This serving determines the cost per 3" serving of sub sandwiches
#Within main(), get the input of the length in inches for the sub and the cost.


#THEN, put the code in main() inside a loop. The loop will ask the user if they want to enter information for another sub sandwich. If so, data is requested and everything including the print statements process again!

def numServings(len):
    servings = len // 3
    return servings

def costPerServing(cost, num):
    price = cost / num
    return price

def main():

    print("This serving determines the cost per 3 inch serving of sub sandwiches")
    price = input("Please enter the price of the sub or press enter to exit. $")
    while price != "":
        length = int(input("Please enter the length of the sandwich you are buying in inches: "))
        print("For your %d inch long sub which is %d servings, you are paying "
              "$%.2f for a cost per serving of $%.2f." % (length, numServings(length), float(price), costPerServing(float(price), numServings(length))))
        price = input("Please enter the price of the sub or press enter to exit. $")

    print("We hope you enjoy your sub.")





main()
