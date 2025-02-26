# if condition:
#   # code blocks 
#   # code blocks
# elif another_condition:
#   # code blocks
#   # code blocks
# else:
#   # default code if all condition fails
#   # code blocks.


# 1. Basic if statement
# x = 10 
# if x > 5:
#   print("x is greater than 5") 

# 2. if-else stmt
# x = 3 
# if x > 5:
#   print("x is greater than 5")
# else:
#   print("x is less than or equal to 5")


# a = 3

# if a < 5:
#     print("x is greater than 5")
#     if a == 3:
#         print("x is equal to 3")
#         if a > 3:
#             print("x is greater than 3")
#         else:
#             print("x is less than 3")
        
# elif a == 10:
#     print("x is equal to")
# else:
#     print("x is less than 5")
    
# # 3. if-elif statement  (if-else if in other languages)


# x = 5 
# if x > 5:
#   print("x is greater than 5")
# elif x == 5:
#   print("x is equal to 5") 
# else:
#   print("x is less than 5")

# 4. Nested if statements
# x = 10
# if x > 5:
#   if x < 15:
#     print("x is between 5 and 15")

# 5 using logical operators (and , or) 

x = 7
if x > 5 and x < 10:
  print("x is between 5 and 10")
  

y = 7 
if x > 5 or x < 10:
    print("x is between 5 and 10")


# 5 Combine if with input (user)
age = input("Enter your age: ") 
age = int(age)
age = int(input("Enter your age: ")) # second way to write input and convert into integer

print(age, type(age))

# if age >= 18:
#   print("You can get a driving license!")
# else:
#   print("Enjoy your bicycle")



# 6 more examples
# short circuiting
# age = int(input("Enter your age: "))

# print(age, type(age))

# if age >= 18 and age <= 22:
#   print("You can get a driving license!")
# else:
#   print("Enjoy your bicycle")


# 7. Checking membership twith 'in'
# fruits = ["apple", "banana", "cherry"] 

# if "banana" in fruits:
#   print("Yes Banana is in the list") 

# if "orange" not in fruits:
#   print("Orange is not in the fruit list)")

# x = False 
# if not x:
#   print("x is False")

# name = "python"
# if  name:
#   print("kya print hoga!")

# if not name:
#   print("print nahi hoga!")


# 9 Ternary Operator
# x = 15
# y = "Even" if x % 2 == 0 else "Odd"

# print(f"{y=}")


# 10 Nested if-else 
# x = 11
# if x > 0:
#     if x % 2 == 0:
#         print("Positive even number")
#     else:
#         print("Positive odd number")

# 11 Multple elif blocks
# marks = 4
# if marks >= 90:
#   print("Grade A")

# elif marks >= 75:
#   print("Grade B")
# elif marks >= 60:
#   print("Grade C")
# else: 
#   print("Fail")
#   print("Are you surprised")

# print("Fail again")


# 12 check empty values

# my_list = [] 
# if my_list:
#   print("The list is empty")

# 13 if with multiple conditions
# x, y = 10, 20 

# print(x)
# print(y)

# if x > 5 and y > 15:
#   print("Both conditions are true")

# Quiz
# a = 10
# b = 20 

# print(a, b)

# To swap two variables

# a = b
# b = a
# print(f"{a=}, {b=}")


# temp = a 
# a = b 
# b = temp 

# print(f"{a=}, {b=}")


# a = 10
# b = 20 
# a, b = b, a

# print(f"{a=}, {b=}")


# 14 Comparing strings
# word = "pYTHon" 
# if word.lower() == "PYThon".lower():
#   print("String matched!")

word = "pYTHon" 
# print(dir(word))

# print(dir([]))


# ==, !=
# a, b = 5, 10 
# if a != b:
#   if a < b:
#     print("a is smaller than b")
#   else:
#     print("a is greater than b")

