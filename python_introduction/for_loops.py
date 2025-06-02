# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#      print(fruit)


# colors = ("red", "green", "blue")
# for one_color in colors:
#   print(one_color)

# message = "Hello, world!"

# for character_inword in message:
#   print(character_inword)

# success = False
# for number in range(1, 6):
#   print("Attempt",number)
#   if success:
#       print("Success on attempt", number)
#       break
# else:
#   print("Failed after 5 attempts")  

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# count = 0
# for even_number in range(1, 10):
#     if even_number % 2 == 0:
#         count += 1
#         print(even_number)

# print(f"we have Total {count} even numbers")

numbers = [1, 5, 3, 9]
total = 0

for number in numbers:
    total = number + number
    print("The current number is:", number)
print("The total is:", total)

