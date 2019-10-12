#Van Nguyen
#2/15/18
#This program determines the shipping cost based on the base cost of a product.

def main():
    print("This program determines the shipping cost based on the base cost of a product.")
    price = float(input("Please enter the price of the purchase: "))
    if (price <= 100):
        shipping = 5
    elif (101 <= price <= 500):
        shipping = 10
    else:
        shipping = 12
    total = price + shipping
    print("Your product, which costs $%.2f  will have a shipping cost of $%.2f for a total of $%.2f" % (price, shipping, total))
main()
