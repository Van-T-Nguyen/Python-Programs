#Van Nguyen
#2/8/2018/
#This program determines pay per week based on hourly wage and hours worked.
#For this assignment, you will create a simple payroll calculator.

#Display your results with clear descriptions.
#The hours worked this week (M through F) are already stored in a list. Please copy this line into your program at the top:
#hours = [7, 8, 12, 0, 8]

#Display an initial message to tell the user the purpose of the program.

#Ask the user to enter:

 #the employee's first name and last name.
 #the hours worked on Saturday. You must append this amount to the list 'hours'. Hours are entered only as whole numbers for this business.  Do not enter '0' - everyone works on Saturday!
 #the employee's hourly wage
#Then...

#Determine the amount earned by summing the hours worked and multiplying by the hourly wage.
#Determine the number of days worked. Hint - remove any day that has the value of 0 and then count the number of items in the list!
#Display the employee's name, total earnings, and number of days worked.

def main():

    hours = [7, 8, 12, 0, 8]
    print("This program determines pay per week based on hourly wage and hours worked.")
    Name = input("Please enter you first and last name: ")
    hours.append(float(input("Please enter the hour(s) worked on Saturday: ")))
    Wage = float(input("Please enter your hourly wage here: "))
    hours.remove(0)
    salary = sum(hours) * Wage
    print(Name+ ", your total pay is", salary, "dollars for working", len(hours), "days.")


main()