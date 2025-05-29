
import random
secret_number = random.randint(1, 50)
print("Secret number", secret_number)
guess = int(input("Guess the secret number between 1 and 50: "))

# -----------------  Using match-case to handle the guess ---------------------

# match guess:
#     case _ if secret_number == guess:
#         print("Congratulations, you guessed it!")
#     case _ if secret_number < guess:
#         print("Your guess is too high.")
#     case _ if secret_number > guess:
#         print("Your guess is too low.") 
#     case _:
#         print("Invalid input. Please enter a number between 1 and 10.")

# -----------------  Using if-elif-else to handle the guess ---------------------

if guess == secret_number:
    print("🎉 Congratulations, you guessed it!")
elif guess > secret_number:
    print("📈 Your guess is too high.")
elif guess < secret_number:
    print("📉 Your guess is too low.")
else:
    print("❌ Invalid input.")

play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != "yes":
        print("👋 Thanks for playing!")
        