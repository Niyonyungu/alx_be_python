# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

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
            temp_str = input("Enter the temperature to convert: ")
            temperature = get_valid_temperature(temp_str)
            
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            while unit not in ['C', 'F']:
                print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            
            if (unit == 'C' and choice == "1") or (unit == 'F' and choice == "2"):
                converted = convert_to_fahrenheit(temperature) if unit == 'C' else convert_to_celsius(temperature)
                out_unit = '°F' if unit == 'C' else '°C'
                print(f"{temperature}°{unit} is equal to {converted:.2f}{out_unit}")
            else:
                print(f"You selected to convert from {'Celsius to Fahrenheit' if choice == '1' else 'Fahrenheit to Celsius'}")
                print(f"but entered a temperature in {'Fahrenheit' if unit == 'F' else 'Celsius'}.")
                print("Please try again with the correct temperature unit.")
                
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()