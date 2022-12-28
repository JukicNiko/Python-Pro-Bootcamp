# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
l_name1 = name1.lower()
l_name2 = name2.lower()

t1 = l_name1.count("t")
r1 = l_name1.count("r")
u1 = l_name1.count("u")
e1 = l_name1.count("e")

l1 = l_name1.count("l")
o1 = l_name1.count("o")
v1 = l_name1.count("v")
e1_1 = l_name1.count("e")

t2 = l_name2.count("t")
r2 = l_name2.count("r")
u2 = l_name2.count("u")
e2 = l_name2.count("e")

l2 = l_name2.count("l")
o2 = l_name2.count("o")
v2 = l_name2.count("v")
e2_2 = l_name2.count("e")

true = t1 + r1 + u1 + e1 + t2 + r2 + u2 + e2
love = l1 + o1 + v1 + e1_1 + l2 + o2 + v2 + e2_2

true_str = str(true)
love_str = str(love)

true_love = true_str + love_str
true_love_int = int(true_love)

if true_love_int < 10 or true_love_int > 90:
    print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int >= 40 and true_love_int <= 50:
    print(f"Your score is {true_love_int}, you are alright together.")
else:
    print(f"Your score is {true_love_int}.")
