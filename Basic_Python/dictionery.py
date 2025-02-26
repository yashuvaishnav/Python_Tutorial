
# Key-value pair data stora

"""
A Python dictionary is a collection of key-value pairs, where 
each key is unique and used to access the corresponding value. 
Dictionaries are mutable, unordered (in Python versions before 3.7), 
and highly optimized for lookups. 

They are defined using curly braces {} or the dict() constructor.

Key Features of Python Dictionaries
- Keys must be immutable (e.g., strings, numbers, or tuples of immutable items).
- Values can be of any data type (mutable or immutable).
- Dictionaries support fast lookups, insertions, and deletions 
  due to their underlying hash table implementation.

"""

# Using curly braces
d1 = {"name": "Alice", "age": 25, "city": "New York"}

# Using the dict() constructor
d2 = dict(name="Bob", age=30, city="San Francisco")

# Empty dictionary
empty_dict = {}


"""
Accessing Values ([] or .get())
- [] raises a KeyError if the key doesn’t exist.
- .get() returns None or a specified default value.
"""

d = {"name": "Alice", "age": 25}
print(d["name"])  # Alice
print(d.get("age"))  # 25
print(d.get("city", "Not Found"))  # Not Found

# ["city"]  ## This will throw KeyError

# Adding or Updating items in dictionary
d = {"name": "Alice", "age": 25}
d["city"] = "Kalyan"  # Add  new key-value pair
d["age"] = 30   # Updating existing value 

print(d)

"""
Deleting Items (del, .pop(), .popitem())
- del removes a key-value pair by key.
- .pop() removes and returns the value for a given key.
- .popitem() removes and returns the last key-value pair (insertion order)

"""

print("Dictionary remove methods")

d = {"name": "Alice", "skill": ["python","js"], "age": 25, "city": "New York"}
print(d)
del d["age"]  # Removes the key "age"
print(d)  # {'name': 'Alice', 'city': 'New York'}

city = d.pop("city")  # Removes "city" and returns its value
print(city)  # New York
print(d)

last_item = d.popitem()  # Removes the last key-value pair
print(last_item)  # ('name', 'Alice')
print(d)


print("--------------")
d = {"name": "Alice", "skill": ["python","js"], "age": 25, "city": "New York"}

print(d["skill"][1])

# Checking existence of a key (in) 
d = {"name": "Alice", "skill": ["python","js"], "age": 25, "city": "New York"}
print("name" in d)   # True (in -> called membership operator)
print("state" in d) # False


"""
 Retrieving Keys, Values, and Items (.keys(), .values(), .items())
- .keys() returns all keys.
- .values() returns all values.
- .items() returns all key-value pairs as tuples.

"""

d = {"name": "Alice", "age": 25}
print(list(d.keys()))  # ['name', 'age']
print(list(d.values()))  # ['Alice', 25]
print(list(d.items()))  # [('name', 'Alice'), ('age', 25)]


tup = (1,2)
tup2 = (True, False) 
tup3 = (5,3,2) 

print(tup[0])  # 1
print(tup2[1]) # False 
print(tup3[2]) # 2

# clear
d.clear() # Remove all items

print(d)

# Iterate over a dictonary
print("Iterating dictionary")
d = {"name": "Alice", "age": 25}
for key in d:
    print(key, d[key])  # name Alice, age 25

for key, value in d.items():
    print(key, value)  # name Alice, age 25


# Dictornary comprehension 
squares = {x: x**2 for x in range(5)}

print(squares)

# Nested dictionaries
nested = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
}
print(nested["person1"]["name"])  # Alice

# len()
print(len(nested))

# sorting keys in  a dict
d = {"b": 2, "a": 1, "c": 3}
sorted_keys = sorted(d)
print(sorted_keys)  # ['a', 'b', 'c']

# Sort dictioary by keys
d = {"b": 2, "a": 1, "c": 3}
sort_by_keys = dict(sorted(d.items()))
print("Sort by keys")
print(sort_by_keys)


# Filtering a Dictionary

d = {"a": 10, "b": 20, "c": 30}
filtered = {k: v for k, v in d.items() if v > 15}
print(filtered)  # {'b': 20, 'c': 30}

