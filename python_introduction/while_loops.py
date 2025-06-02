# age = 0

# while age < 18:
#   age = int(input("Enter your age (must be 18 or older): "))
# print("You are old enough to proceed.")

# secret_number = 7

# guess_count = 0
# guess = 0

# while guess != secret_number:
#   guess_count += 1
#   guess = int(input("Guess a number between 1 and 10: "))

# print(f"You guessed it in {guess_count} tries!")


# shopping_list = ["apples", "bread", "milk", "cheese"]
# item_found = False

# while not item_found:
#   item = input("Search for an item in your list (or 'q' to quit): ")
#   if item.lower() == "q":
#     break  
#   if item in shopping_list:
#     item_found = True
#     print(f"{item} is/are on your shopping list.")
#   else:
#     print(f"{item} is/are not on your shopping list.")

# i = 2
# while i <= 5:
#     print(i, end=' ')
#     j = 2
#     while j <= 4:
#         print(j, end=' ')
#         j += 1
#     i += 1
#     print() 


# outer_count = 5

# while outer_count > 0:
# #   Outer loop controls the number of times the inner loop runs
#   inner_count = 1
#   while inner_count <= outer_count:
#     # Inner loop repeats for each outer loop iteration
#     print(inner_count, end=" ")
#     inner_count += 1
#   print()  # Move to a new line after each outer loop iteration
#   outer_count -= 1

# for i in range(1, 11):
#   # Outer loop iterates through rows (multiplication factors)
#   for j in range(1, 11):
#     # Inner loop iterates through columns (other factors)
#     product = i * j
#     print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
#   print()  # Move to a new line after each row


# rows = 5

# for i in range(1, rows + 1):
#   # Outer loop controls the number of rows
#   for j in range(1, i + 1):
#     # Inner loop prints asterisks for each row
#     print("*", end="")
#   print()  # Move to a new line after each row of asterisks


# nested while loop (a while loop inside the body of another while loop)

# list1 = [1, 2, 3]
# print("length of list1 is:" ,len(list1))
# list2 = [4, 5, 6]

# i = 0
# while i < len(list1):
#     j = 0
#     while j < len(list2):
#         print(list1[i], list2[j])
#         j += 1
#     print()  # Print a new line after inner loop completes
#     i += 1



rows = 5
row = 1

while row <= rows:
    # Print spaces
    space = 1
    while space <= rows - row:
        print(" ", end="")
        space += 1

    # Print asterisks
    star = 1
    while star <= 2 * row - 1:
        print("*", end="")
        star += 1

    # Move to next line after each row
    print()
    row += 1
