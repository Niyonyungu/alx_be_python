# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def get_valid_temperature(temp_str):
    """Validate and convert temperature input to float."""
    try:
        return float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    while True:
        try:
            print("\nTemperature Conversion Tool")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "3":
                print("Thank you for using the Temperature Conversion Tool!")
                break
                
            if choice not in ["1", "2"]:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            
            temp_str = input("Enter the temperature: ")
            temperature = get_valid_temperature(temp_str)
            
            if choice == "1":
                converted = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is equal to {converted:.2f}°F")
            else:
                converted = convert_to_celsius(temperature)
                print(f"{temperature}°F is equal to {converted:.2f}°C")
                
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()