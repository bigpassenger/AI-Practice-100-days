# # # # # # # # # # # # # # # # List in pythons # # # # # # # # # # # # # # # # 
"""
In Python, a list is an ordered, mutable collection of elements.
Think of it like a flexible container that can hold any type of data, and you can change it at will.

Key Points About Lists:

    1.Ordered → Elements maintain the order you define.

    2.Mutable → You can add, remove, or change elements after creation.

    3.Can contain different data types → integers, strings, floats, even other lists.

    4.Allow duplicates → The same value can appear multiple times.

    5.Indexable & Slicable → You can access parts of the list using indexes.
"""
# numbers = [1,2,3,4]

# fruits = ["apple", "banana", "cherry"]

# mixed = [1, "apple", True]

# print(numbers[2])
# print(fruits[0])
# print(mixed[1])
# print(fruits[-1]) 

# fruits.append("orange")
# fruits(1, "grape") #["apple", "grape", "banana", "cherry", "orange"] insert at index 1

# fruits.remove("banana") #["apple", "grape", "cherry", "orange"] 

# del fruits[0] # [ "grape", "cherry", "orange"] similar to fruits.remove(apple)

# fruits.pop() # Will pop items from last elements [ "grape", "cherry"]

# # # Slice a list
# fruits = ["apple", "grape", "banana", "cherry", "orange"]
# sliced_fruits = fruits[2:4]


# # # # # # # # # # # # # # # # Tuple in pythons # # # # # # # # # # # # # # # # 
"""
In Python, a tuple is an ordered, immutable collection of elements.
Think of it like a list, but once you create it, you can’t change its contents (no adding, removing, or modifying elements).

Key Points About Tuples:

    1.Ordered → Elements maintain the order you define.

    2.Immutable → After creation, you can’t change elements.

    3.Can contain different data types → integers, strings, floats, objects, etc.

    4.Allow duplicates → Same value can appear multiple times.

    5.Indexable & Slicable → You can access elements by index or slice
"""
# colors = ("red", "green", "blue")
# single_item_tuple = ('grass', ) #for creating a single item tuple we need to put a omma at the end
# a_tuple_with_a_list = ('null', [1,2,3])
# print(a_tuple_with_a_list[0])
# print(a_tuple_with_a_list[1])
# a_tuple_with_a_list[1].remove(2)
# print(a_tuple_with_a_list)


# # # # # # # # # # # # # # # # Dictionary in python # # # # # # # # # # # # # # # # 

"""
In Python, a dictionary (dict) is an unordered, mutable collection of key–value pairs.
Think of it like a real dictionary: you look up a word (key) to find its meaning (value).

Key Points About Dictionaries:

    1.Key–Value Storage → Each value is stored under a unique key.

    2.Mutable → You can add, change, or remove key–value pairs.

    3.No duplicate keys → A key must be unique; if you add the same key again, the old value is replaced.

    4.Keys must be hashable → Typically strings, numbers, or tuples (not lists or other dicts).

    5.Values can be any type → Numbers, strings, lists, other dictionaries, etc.
"""

# student = {"name": "Alice", "age": 25, "grade": "A"}
# print(student["age"])
# print(student["grade"])
# student["subject"] = 'Math'
# student["age"] = 32 # Update a key and value
# del student["grade"]
# student.pop("subject") ## in dictionary you have to calarify the KEY IN THE POP FUNCTION!
# print(student)

# # # # # # # # # # # # # # # # iteration in a dic # # # # # # # # # # # # # # # # 
# student = {"name": "Alice", "age": 25, "grade": "A"}
# for key, value in student.items():
#     print(key+":"+str(value))

# # # # # # # # # # # # # # # #  Sets in python # # # # # # # # # # # # # # # # 
"""
In Python, a set is an unordered, mutable collection of unique elements.
It’s like a mathematical set: no duplicates, and the order doesn’t matter.

Key Points About Sets:

    1.No duplicates → Each element is unique.

    2.Unordered → Elements don’t have a fixed position (so you can’t rely on indexing).

    3.Mutable → You can add or remove elements.

    4.Elements must be hashable → Numbers, strings, tuples are fine; lists and dictionaries are not.

    5.Optimized for fast membership checks → Great for “Does X exist?” type operations.


"""
# Creating a Set

# numbers = {1, 2, 3, 4}

# # Empty set (must use set(), not {})
# empty_set = set()

# # Adding and removing in set??
# print(numbers)
# numbers.add(5)
# print(numbers) #-> {1, 2, 3, 4, 5}
#     # numbers.add(5) # ->{1, 2, 3, 4, 5} # Duplicate items won't add anything in a sets
#     # print(numbers)
# numbers.remove(5)
# print(numbers)

# # # Union
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1|set2)

# # # # Intersection
# print(set1&set2)

# # # # Difference
# print(set1 - set2)


################################### EXERCISE 1: MANIPULATE DATA IN A DICTIONARY ###################################
# person = {'Name':"Amin",
#        'Major':"Optics",
#        'age':"24",
#         "Being_single":True,
#         "Attractive":True,
#         }
# for key, value in person.items():
#     if key == 'Major':
#         if value == "Optics":
#             person['Major'] = "Computer"

# # print(person)

# #Add new value
# person['psychology_item'] = "Deppresion"

# # print(person)

# # Update dictionary
# if person['Major'] == "Computer":
#     person['psychology_item'] = "Happines"

# # print(person)

# #Delete an item
# if person["Attractive"] == True:
#     del person["Being_single"]

# print(person)


################################### EXERCISE 1: Word Frequency Counter ###################################
# words = {}

# sentence = str(input())

# splited = sentence.split(' ')

# for each in splited:
#     each = each.lower()
#     count = 0
#     words[each] = 0
#     for each2 in splited:
#         if each == each2:
#             count +=1
#     words[each] = count

# print(words)
##########################################################################################################
reversed = ['Book', 'Weed', 'Wood', 'Road', 'Wood', 'Wood']
reversed.reverse()
reversed_set = set(reversed)
print(reversed_set)