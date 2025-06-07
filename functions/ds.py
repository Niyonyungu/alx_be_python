"""
Data Structure :
a way of storing data 
  - List 
  - Tuples 
  - Sets 
  - Dictionaries 

lists are mutable, ordered collections of items
tuples are immutable, ordered collections of items 
sets are unordered collections of unique items 
dictionaries are unordered collections of key-value pairs

"""

# Lists are mutable, ordered collections of items
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('orange')  

# second_item = fruits[1]  
# print(second_item[0]) 
# print(type(fruits)) 

# print(len(fruits))  

# # Tuples are immutable, ordered collections of items
# fruits_tuple = ('apple', 'banana', 'cherry')
# print(type(fruits_tuple))
# # fruits_tuple[0] = 'orange' # This will raise an error because tuples are immutable
# print(fruits_tuple)


# Sets are unordered collections of unique items
# unique_numbers = {1, 2, 3, 4, 5}
# unique_numbers.add(6)  # Adding an item to the set
# print(unique_numbers)
# print(type(unique_numbers))

# Dictionaries are unordered collections of key-value pairs
person = {"name": "John", "age": 30, "city": "New York"}
print(person.get("name"))  # Accessing value by key

print(person.items())  # Accessing value by key