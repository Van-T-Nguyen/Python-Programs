#Van Nguyen
#3/29/2018
#This program prints out the first and last name, hours, and pay rate of a worker based on data entered into a list





#Add a function that will calculate and return the total pay. You do not need to store total pay in a list. Just call the function from within the loop either before the print statement or within the print statement. Display the pay amount using a preceeding $ and two decimal points. You should now have something like this:
#Joe Smith 40 10 $400.00

#Force the input for the employee's name to all caps. It is also important to use field widths and align financial data to the right. You should now have something like this:

#JOE       SMITH       40      10      $400.00

#It is important that you strip the data of all preceeding and following spaces (white space) which can effect string data. Do this for all the data that has a data type of string. Test by adding a couple preceding and following spaces to all the data you input. If done correctly, the display will have only one space between each piece of data and there will be no error messages.

#Now, make the output look nice. Add field widths so that the data is nicely formatted. Once it looks good, you are done!!!
def main():
    print("This program prints out the first and last name, hours, and pay rate of a worker based on data entered into a list.")
    fname = []
    lname = []
    hours = []
    payrate = []


    first_name = input("Please enter your first name or press enter to exit: ")
    while first_name != "":
        last_name = input("Please enter your last name: ")
        hrs = int(input("Please enter hours worked: "))
        pay = float(input("Please enter your pay per hour: "))
        fname.append(first_name.strip().upper())
        lname.append(last_name.strip().upper())
        hours.append(hrs)
        payrate.append(pay)
        total = hrs * pay
        first_name = input("Please enter your first name or press enter to exit: ")

    for x in range(len(fname)):
            print("%-10s %-10s %3d $%.2f $%.2f" % (fname[x], lname[x], hours[x], payrate[x], total))
main()