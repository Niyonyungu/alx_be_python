# pattern_drawing.py

# Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print asterisk without a newline
    print()  # Move to the next line after each row
    row += 1  # Increment row counter
