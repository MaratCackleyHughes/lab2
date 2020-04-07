__author__ = 'Marat Cackley-Hughes'

#Input list: gallon_price, tank_size
#Output list: gallon_price, tank_size, total_fillup
#Declare Real gallon_price
#Declare Real tank_size
#Declare Real total_fillup

#Display welcome message
#Display "Enter gallon price"
#Input gallon_price
#Display "Enter gas tank size"
#input "tank_size"
#
#
#Set total_fillup = gallon_price * tank_size
#Display "You entered a gallon price of " + gallon_price
#Display "You entered a tank size of " + tank_size

#Display "you total fill up price would be " + total_fillup price

gallon_price = 0.0
tank_size = 0.0
total_fillup = 0.0
print(" Welcome to our gas price calcuator.")
print(" Please enter your price per gallon,")
print(" and then your gas tank deposit size,")
print(" I'll then tell you the total cost of filling up your tank.")
print("")

gallon_price = float(input("Please enter the price per gallon:"))
tank_size = float(input("Please enter your gas tank deposit size:"))

total_fillup = gallon_price * tank_size

print("The total price of filling up you tank is: $", total_fillup)
print("Thank you for using our gas price calculator and please drive defensively ")
