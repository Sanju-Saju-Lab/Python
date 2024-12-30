# Define the color codes for the resistor bands
COLOR_CODES = {
    "black": 0, "brown": 1, "red": 2, "orange": 3,
    "yellow": 4, "green": 5, "blue": 6, "violet": 7,
    "gray": 8, "white": 9
}

# Define the multipliers for each color
MULTIPLIERS = {
    "black": 1, "brown": 10, "red": 100, "orange": 1_000,
    "yellow": 10_000, "green": 100_000, "blue": 1_000_000,
    "gold": 0.1, "silver": 0.01
}

# Define the tolerance values for each color
TOLERANCE = {
    "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
}

# Function to calculate resistance based on color bands
def calculate_resistance():
    # Display available colors for the first and second band
    print("\nAvailable colors for 1st and 2nd band:")
    print(", ".join(COLOR_CODES.keys()))  # Display color names for first and second band
    band1 = input("Enter the 1st color: ").strip().lower()  # Get user input for first color
    band2 = input("Enter the 2nd color: ").strip().lower()  # Get user input for second color

    # Display available multiplier colors
    print("\nAvailable multiplier colors:")
    print(", ".join(MULTIPLIERS.keys()))  # Display color names for multipliers
    multiplier = input("Enter the multiplier color: ").strip().lower()  # Get user input for multiplier

    # Display available tolerance colors
    print("\nAvailable tolerance colors:")
    print(", ".join(TOLERANCE.keys()))  # Display tolerance color names
    tolerance = input("Enter the tolerance color: ").strip().lower()  # Get user input for tolerance

    # Validate inputs and calculate resistance if valid
    if band1 in COLOR_CODES and band2 in COLOR_CODES and multiplier in MULTIPLIERS:
        # Calculate resistance based on input colors
        resistance = (COLOR_CODES[band1] * 10 + COLOR_CODES[band2]) * MULTIPLIERS[multiplier]
        tolerance_value = TOLERANCE.get(tolerance, "Unknown tolerance")  # Get tolerance if valid
        print(f"\nResistance: {resistance} Ω {tolerance_value} "
              f"(Bands: {band1}, {band2}, {multiplier}, {tolerance})")
    else:
        print("\nInvalid color code entered. Please try again.")  # Error message for invalid input

# Function to suggest resistor color bands based on a given resistance value
def suggest_color():
    # Input resistance value from the user
    try:
        resistance = float(input("\nEnter the resistance value in Ω: ").strip())  # Convert input to float
        tolerance = input("Enter the tolerance (1%, 2%, 5%, or 10%): ").strip().lower()  # Get tolerance input

        # Check for matching color bands
        for band1, digit1 in COLOR_CODES.items():
            for band2, digit2 in COLOR_CODES.items():
                for multiplier_color, multiplier_value in MULTIPLIERS.items():
                    # Check if the resistance calculated matches the entered value
                    if abs((digit1 * 10 + digit2) * multiplier_value - resistance) < 0.001:
                        # Find the color corresponding to the tolerance
                        tolerance_color = next((k for k, v in TOLERANCE.items() if v == f"±{tolerance}%"), None)
                        if tolerance_color:
                            print(f"\nColor Bands: {band1}, {band2}, {multiplier_color}, {tolerance_color} "
                                  f"(Resistance: {resistance} Ω ±{tolerance}%)")
                            return  # Exit once the correct color bands are found
                        else:
                            print("\nInvalid tolerance value entered.")  # Error message for invalid tolerance
                            return
        print("\nNo matching color code found.")  # If no match is found, display this message
    except ValueError:
        print("\nInvalid resistance value. Please enter a numeric value.")  # Error for invalid resistance input

# Main program loop for interacting with the user
while True:
    # Display the menu of options
    print("\nChoose an option:")
    print("1. Calculate resistance from color bands.")
    print("2. Suggest color bands from resistance.")
    print("3. Exit")

    # Get user choice
    choice = input("Enter your choice: ").strip()

    # Call the appropriate function based on the user's choice
    if choice == "1":
        calculate_resistance()  # Calculate resistance from color bands
    elif choice == "2":
        suggest_color()  # Suggest color bands from resistance
    elif choice == "3":
        print("\nExiting the program. Goodbye!")  # Exit the program
        break  # End the loop and stop the program
    else:
        print("\nInvalid choice. Please try again.")  # Error message for invalid menu choice
