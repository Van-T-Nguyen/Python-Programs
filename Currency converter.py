#Van Nguyen
#2/1/2018

def main():
    print("This program converts US dollars to Euros, Pounds, and Canadian Dollars.")
    US_Dollars = float(input("Please enter the amount of money in US dollars: "))
    Euros = US_Dollars * .79948
    Pounds = US_Dollars * .70096
    Canadian_Dollars = US_Dollars * 1.22647
    print("Your amount of " + str(US_Dollars) + " dollars are equivalent to: " + str(Euros) + " Euros, "
          + str(Pounds), "Pounds, and " + str(Canadian_Dollars) + " Canadian Dollars.")

main()