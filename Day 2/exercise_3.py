# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

int_age = int(age)

until_90 = (90 - int_age)

months = (until_90 * 12)
days = (until_90 * 365)
weeks = (until_90 * 52)

print(f"You have {days} days, {weeks} weeeks, and {months} months left.")