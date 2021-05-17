#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Intro to Program
print("Welcome to the tip calculator.")

#Total_bill variable
total_bill= float(input("What was the total bill? $"))

#Tip percentage variable
percentage_tip= float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

#Size of party variable
party_size= int(input("How many people to spilt the bill? "))


#Create variable total bill + tip
total_bill_with_tip= (total_bill * percentage_tip) + total_bill


#Calculate the amount of tip per person
tip_per_person= total_bill_with_tip/ party_size


#Print the amount of each person should pay
print(f"Each person should pay: ${tip_per_person: .2f}")
