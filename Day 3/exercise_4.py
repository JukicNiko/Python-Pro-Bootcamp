#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("What was the total bill? ")
tip = input ("What percentage would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

float_bill = float(bill)
int_tip = int(tip)
int_people = int(people)

payment = (float_bill / int_people) * ((100 + int_tip) / 100)

print(f"Each person should pay ${round(payment,2)}")