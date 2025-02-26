# Example of creating a list 
# List is mutable 
fruits = ["apple", "orange", "chickoo","grapes"]

everything = ["apple", "orange", 10, 20, True, False]

# print(fruits) 
print(everything[5])

print(fruits[0])

# print(fruits[1])

# print(everything[3])

# # last element
# print(fruits[3])
# print(everything[5])

# negative indexing
# print(fruits[-1])
# print(everything[-1])

# # second last element
# print(fruits[-2])
# print(everything[-2])

# # Slice 

# nums = [22,23,24,25,26,27]

# nums[start:end:step]
# print(nums[0:4:2]) # end - Isme element exclude hota he


# nums[start:end:step]    # start -> index to begin, end-> last index excluding end, step->Skip

# print(nums[3:])
# print(nums[0:11:2])

# # Operatons on array
# # insert, append, remove, edit
# print(nums)
# nums = [0,1,2,3,4,5,6,7,8,9,10]

# listElements = [1,2,3,4]

# listElements.append("yash")
# nums[1] = "hello" 
# print(listElements)

# listElements.insert(1, "yash")
# print(listElements)
# listElements()

# num = listElements.pop(1)
# print(num)

# ele = nums.pop(3)

# print(f"{last=}")
# listElements.remove(3)
# nums.remove(6)  # remove first occurence of value 6

# print(listElements)


# nums.append(11)

# print(nums)

# # insert at index
# nums = [0,1,2,3,4,5,6,7,8,9,10]
# insert(index,value)
# nums.insert(1, 99)
# print(nums)

# remove last elem by default
# nums = [0,1,2,3,4,5,6,7,8,9,10]
# last = nums.pop()
# print(f"{last=}")

# print(f"{nums=}")
# nums.pop(index)  # indexing based pop element
# ele = nums.pop(3)
# print(f"{ele=}")
# print(f"{nums=}")

# remove element directly
# nums = [0,1,2,3,4,5,6,7,8,9,10]
# nums.remove(ele) # jo elements hme remove krna he direcly
# nums.remove(5)
# print(nums)

# # nums.remove(1000) # error as element is not present

# edit
# nums = ["yash","shiddhant","bhavna"]
# nums[1] = "hello" 
# print(nums)

# # nums.remove(6)  # remove first occurence of value 6


# # finding duplicate elements, remove duplicate and sort the list by ascending
# nums = [1, 6, 4, 3, 5, 1, 6]
# nums = list(set(nums))
# print(nums)
# nums.remove(6)  # remove first occurence of value 6
# print(nums)
# # finding elements
# # using index
# nums = [1, 6, 4, 3, 5, 1, 6]
# nums.index(element)
# idx = nums.index(6)  # element ka index show kr rha he
# print(f"{idx=}")

# # # count
# nums = [1, 6, 4, 3, 5, 1, 6]
# # print(nums.count(3))
# print(nums.sort())



# print(f"{nums.count(4)=}") # element count krta he kitne he
# print(f"{nums.count(6)=}")

# # remove
# nums.remove("hello")
# print(nums)

# nums.append(13)
# nums.append(22) 
# nums.append(12)

# print(nums)
# # # sort -> by default asc, mutable operation
# nums = [1, 6, 4, 3, 5, 1, 6]
# nums.sort(reverse=True) 
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# multiple types of elements in list
# nums = [1, 6, 4, 3, 5, 1, "hello"]

# nums.sort()   # error because heterogenous elements in list 
# print(nums)

# # convert all elements to strings for sorting 
# nums.sort(key=str)
# print(nums)



# Useful functions
# print(type(1))
# print(type("nums"))
# print(type(True))
# print(type(1.2))



# # Nesting list 
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

# print(nested_list[0])
# print(nested_list[1])
# print(nested_list[1][0])

# print(nested_list[:2])


# //////////////////////////////////////////////////////////
# # List comprehensiion
print(nested_list[1])

# # Useful function
# # range()

# print(range(4))

# elems = [x for x in range(5)]
# print(elems)

# squared = [x**2 for x in elems]
# print(f"{squared=}")

# nums = [1, 6, 4, 3, 5, 1, 6]
# something = [n for n in nums]
# print(something)

# nums = [6, 4, 3, 5, 1, 6]
# squared = [n**2 for n in nums]
# print(squared)  # Output: [36, 16, 9, 25, 1, 36]


# # flatten
# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# flattened = [n for n in list and list for item in n]
# flattened = [item for sublist in nested_list for item in sublist]
# print(f"{flattened=}")

# Logic 
# flattened = [] 
# for sublist in nested_list:  # outer loop 
#   for item in sublist:  # inner 
#     flattened.append(item)
# print(flattened)

# # [expression for outer_loop for inner_loop]



