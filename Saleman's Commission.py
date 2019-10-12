#Van Nguyen
#2/22/2018
#This program calculates how much a salesman
#  makes in commission based on his weekly sales



#     loop 7 times
#           Enter sales for day x
#           total = total + sales

#    calculate the commission
#    print the total and the commission

def main():
    print("#This program calculates how much a salesperson"
          " makes in commission based on their weekly sales.")
    name = input("Please enter the name of the salesperson: ")
    total = 0
    sales1 = float(input("Please input the sales for Monday here: $"))
    sales2 = float(input("Please input the sales for Tuesday here: $"))
    sales3 = float(input("Please input the sales for Wednesday here: $"))
    sales4 = float(input("Please input the sales for Thursday here: $"))
    sales5 = float(input("Please input the sales for Friday here: $"))
    sales6 = float(input("Please input the sales for Saturday here: $"))
    sales7 = float(input("Please input the sales for Sunday here: $"))
    sales = [sales1, sales2, sales3, sales4, sales5, sales6, sales7]
    for x in (sales):
        total = total + x
        commissions = total * .10
    print("%s, you have made $%.2f in commissions for $%.2f of total sales." % (name, commissions, total))


main()