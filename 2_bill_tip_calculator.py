#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill = input("What is your total bill?\n $")
tip_percentage = input("What is the percentage tip that you would like to give? 10, 12 or 15?\n ")
people = input("How many people do you want to split the bill with?\n ")
# can also do float(input(....))          which is cleaner

bill_plus_tip = float(total_bill) * ( 1 + (float(tip_percentage)/100))

split_bill = bill_plus_tip / int(people)
rounded_split_bill = round(split_bill, 2)

print("Each of you should pay $" + "{:.2f}".format(rounded_split_bill))