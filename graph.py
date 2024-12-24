import matplotlib.pyplot as plt

# Function to get the title of the graph from the user
def get_title():
    title = input("Enter the title of the graph: ")  # Asking user for the graph title
    return title

# Function to get labels for the X and Y axes from the user
def get_axis_labels():
    x_label = input("Enter the label for the X-axis: ")  # Asking user for the X-axis label
    y_label = input("Enter the label for the Y-axis: ")  # Asking user for the Y-axis label
    
    # Set default labels if the user doesn't provide any
    if not x_label:
        x_label = "X-axis"  # Default label for X-axis
    if not y_label:
        y_label = "Y-axis"  # Default label for Y-axis
    
    return x_label, y_label  # Return the labels

# Function to get coordinates from the user
def get_input():
    coordinates = input("Enter the x and y coordinates (x,y): ")  # Asking user to enter coordinates
    
    x = []  # List to store the X values
    y = []  # List to store the Y values
    
    # Split the input into individual coordinate pairs
    coordinate_pairs = coordinates.split()  # Split the input string by spaces
    
    # Loop through each coordinate pair
    for coordinate in coordinate_pairs:
        try:
            # Remove parentheses and split by comma to separate X and Y values
            coordinate = coordinate.strip('()')  # Remove parentheses
            x_value, y_value = coordinate.split(',')  # Separate X and Y values by comma
            
            # Convert the values to floats and add them to the lists
            x.append(float(x_value))  # Add X value to the list
            y.append(float(y_value))  # Add Y value to the list
        except ValueError:
            # Print an error message if the format is invalid
            print(f"Invalid coordinate format: {coordinate}")
            continue  # Skip to the next coordinate if there's an error
    
    return x, y  # Return the X and Y lists

# Get the graph title from the user
title = get_title()  # Get the graph title

# Get the X and Y axis labels from the user
x_label, y_label = get_axis_labels()  # Get the labels for X and Y axes

# Get the coordinates (X and Y values) from the user
x, y = get_input()  # Get the coordinates from the user

# Check if the number of X and Y values are the same
if len(x) != len(y):
    print("Error: The number of x and y values must be the same.")  # Error message if number of X and Y values don't match
else:
    # Set the title and labels for the graph
    plt.title(title)  # Set the title of the graph
    plt.xlabel(x_label)  # Set the label for the X-axis
    plt.ylabel(y_label)  # Set the label for the Y-axis
    
    # Plot the X and Y values on the graph
    plt.plot(x, y)  # Create the line plot with X and Y values
    
    # Add grid lines to the graph for better readability
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add grid lines
    
    # Display the graph
    plt.show()  # Show the graph to the user
