# age = 0 
# # if age < 18:
# #     message = "You are a minor."
# # else:
# #     message = "You are an adult."
# message = "You are a minor." if age < 18 else "You are an adult."
# print(message)
# # and operators
# high = True
# high2 = False
# if high and high2:
#     print("Both conditions are true.")  
# else :
#     print("At least one condition is false.")

# # Using the 'or' operator

# high = True
# high2 = True 
# if high or high2:
#     print("At least one condition is true.")

# # Using the 'not' operator
# high = False
# high2 = False
# if not high:
#     print(f"The {high} is false.")

# high_income = True
# good_credit = False
# isstudent = False

# if (high_income or good_credit) and not isstudent:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# chain comparasion
# age = 22  
# if 18 <= age < 65:
#     print("You are an adult.")

# Match case

# day = input("Enter a day of the week (Monday-Sunday): ").lower()

# match day:
#     case "monday":
#         print("Ugh, Mondays...")
#     case "tuesday":
#         print("Just another workday...")
#     case "wednesday":
#         print("Hump day!")
#     case "thursday":
#         print("Almost there...")
#     case "friday":
#         print("TGIF!")
#     case "saturday" | "sunday":  # Match multiple values with pipe (|)
#         print("Weekend vibes!")
#     case _:
#          print("Invalid day entered.")

# user_input = input("Enter a value (number or string): ")

# try:
#     value = int(user_input)
# except ValueError:
#     value = user_input

# match value:
#     case int():
#         print("You entered an integer:", value)
#     case str():
#         print("You entered a string:", value)
#     case _:
#         print("Unknown type.")



# age = int(input("Enter your age: "))

# match age:
#     case 18 | 19:  # Match multiple values with pipe (|)
#         if age >= 18 and has_id(user):  # Guard using a function call
#             print("You are eligible to vote.")
#         else:
#             print("You need a valid ID to vote.")
#     case _:
#         print("You are not yet eligible to vote.")

