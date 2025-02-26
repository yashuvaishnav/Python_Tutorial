"""
What is a Function?
A function is a block of reusable code that performs a specific task

"""

# def function_name(parameters = "optional"):
  # Code block
  # return None 
  # print("hello world")

# Outside function
# result = function_name()
# print(result)

# def f1_with_one_para(a):
#   print(a) 

# f1_with_one_para(5)

# def f1_with_two_para(a, b):
#   return a + b

# result = f1_with_two_para(5,2)
# print(result)


# default parameter
# def power(base = 2, exp = 2):
#   return base ** exp

# print(power(3))    # -> 9
# print(power(3, 2)) # -> 9 
# print(power(2, 3)) # -> 8 

# print(power())

# def heading(text, char = "-"):
#   print(text)
#   print(char * 20)

# Variable scoping
# heading("Variable scope", "*")
# x = 10  # Global variable

# def modify_var():
#   global x
#   x = 5
#   print("Inside function....", x)

# modify_var()
# print("Outside function...", x)


# Lambda function
"""
What is a Lambda Function?
A lambda function is an anonymous, inline function

"""

# heading("Lambda functons...")
# square = lambda x: x * x 

# print(square(4))

# heading("Lambda function: Multiple arguments")
# add = lambda a, b: a + b 
# print(add(5, 3))

# heading("Higher Order Functions") 
# def apply_func(func, value):
#   return func(value)

# result = apply_func(lambda x: x * 2, 5)

# print("Result: ", result)


# heading("Returning functions from function")
# def multiplier(factor):
#   return lambda x: x * factor 

# double = multiplier(2)

# print(double)

# print(double(10))
# print(double(2))

# triple = multiplier(3)
# print(triple) 
# print(triple(2))


# heading("Using map") 
# numbers = [1,2,3,4]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled) 


# heading("Using filter") 
# numbers = [1,2,3,4]
# even_nos = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_nos)


# heading("Recursive function")
# """
# Factorial:  4  = 4 * 3 * 2 * 1
# 5 = 5 * 4!
# """

# def factorial(n):
#   if n == 1:
#     return 1
#   return n * factorial(n - 1)

# print("Factorial (1): ", factorial(1))
# print("Factorial (2): ", factorial(2))
# print("Factorial (3): ", factorial(3))


# # Variable length arguments
# def sum_all(*args):
#   print(args)
#   total = 0
#   for value in args:
#     total = total + value
#   return (sum(args), total)
  # return sum(args)
  

# print(sum_all(1,2,3,4,5))
# print(sum_all(2,4,5))
# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5,6,7,8,9,2,4,54,66))

# sm, total = sum_all(1,2,3) 
# print(sm, total)

# result = sum_all(1,2,3)
# print(result)



# kwargs
# def print_kv(**kwargs):
#   print(kwargs)
#   for key, value in kwargs.items():
#     print(f"{key} : {value}")

# print_kv(name="Python", lang_type="High Level")
# print_kv(first_name="Amit", percent="80", grade="A")


# Assignment -> multiply all arguments
# def mul(*args):
#     result = 1
#     for number in args:
#         result *= number
#     return result    

# print(mul(2,3))
# print(mul(2,3,4,5))


