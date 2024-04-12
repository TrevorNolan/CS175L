def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    # Convert Fahrenheit to Kelvin
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def convertToCentigrade(fahrenheit):
    # Convert Fahrenheit to Centigrade
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade

def doConversion():
    fahrenheit = getFahrenheit()
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f"Fahrenheit: {fahrenheit} Kelvin: {kelvin} Centigrade: {centigrade}")

def repeat():
    num_conversions = int(input("How many conversions would you like to do this time? "))
    for _ in range(num_conversions):
        doConversion()

def controlLoop():
    while True:
        choice = input("Do you want to do some conversions (Yes or No)? ").lower()
        if choice == 'yes':
            repeat()
        elif choice == 'no':
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def getFahrenheit():
    while True:
        try:
            fahrenheit = float(input("Enter Fahrenheit temperature (must be -50 to 130): "))
            if -50 <= fahrenheit <= 130:
                return fahrenheit
            else:
                print("Temperature must be between -50 and 130.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
