# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days= (365 * 90) -(365 * int(age))
weeks= (52 * 90) - (52 * int(age))
months= (12 * 90) - (12 * int(age))

print(f"You have {days} days, {weeks} weeks, {months} months left.")

#Another solution for this challenge:
print("\n Here is your answer again.\n")

age_as_int= int(age)

years_remaining= 90 - age_as_int
days_remaining= years_remaining * 365
weeks_remaining= years_remaining * 52
months_remaining= years_remaining * 12

message= f" You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months."

print(message)
