# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_height = float(height)
int_weight = int(weight)

BMI_calculation = (int_weight / (int_height ** 2))
print(int(BMI_calculation))