# For loops
# # Basic

# numbers = [1,2,3,4,5]

# # print(numbers[0])
# # print(numbers[1])

# for number in numbers:
#   print(number)

# # range()
# for i in range(5):
#   print(i)


# # string

# for idx in 'hello':
#   print(idx)

# # for num in 123:
# #   print(num)

# print(dir('hello'))

# print(type('hello'))

# Enumerate -> if we need to take index and value from loop that time we can use enumerate built-in function in python It will take two value first one the element and second one the index from which we need to show.

# compare with this for loop 

# fruits_list = ['apple', "orange", "jalebi"]
# for i in fruits_list:
#         print(i)

# example  enumerate(fruits,1)fruits
# for index, fruits_element in enumerate(fruits_list, 1):
#   print(f"{index}. {fruits_element}")


# Nested loop

# for i in "abc":  # first loop
#         # i=3
#     for j in "z": # second loop
        #  j=1
        # print(f"i={i}, j={j}")  # 1) i=0 , j=0 2) i=0,j=1 3) i=1,j=0 4) i=1,j=1 5) i=2,j=0 6) i=2,j=1


# break and continue


# for idx in range(5):
#   if idx == 4: 
#     break
#   print(idx)

# for number in range(5): # 0 1 3
#   if number == 2:
#     continue
#   print(number)



# WHITE LOOP
# count = 0 
# while count <= 5:
#   print(count)
#   count += 2 # count = count + 1

# count = 5 
# while count > 0:
#   print(count)
#   count -= 1

# Quiz

# while True:
#   response = input("Type 'exit' to quit: ")
#   if response.lower() == 'exit':
#       break 


# Quiz
# items = [1,2,3]
# while items:
#     item = items.pop()
#     print(item)



