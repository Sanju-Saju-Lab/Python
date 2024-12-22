import matplotlib.pyplot as plt

# Function to get the title of the graph from the user
def get_title():
    title = input("Enter the title of the graph: ")
    return title

# Function to get labels for the X and Y axes from the user
def get_axis_labels():
    x_label = input("Enter the label for the X-axis: ")
    y_label = input("Enter the label for the Y-axis: ")
    
    # Set default labels if the user doesn't provide any
    if not x_label:
        x_label = "X-axis"
    if not y_label:
        y_label = "Y-axis"
    
    return x_label, y_label

# Function to get coordinates from the user
def get_input():
    coordinates = input("Enter the x and y coordinates (x,y): ")
    
    x = []  # List to store the X values
    y = []  # List to store the Y values
    
    # Split the input into individual coordinate pairs
    coordinate_pairs = coordinates.split()
    
    # Loop through each coordinate pair
    for coordinate in coordinate_pairs:
        try:
            # Remove parentheses and split by comma to separate X and Y values
            coordinate = coordinate.strip('()')
            x_value, y_value = coordinate.split(',')
            
            # Convert the values to floats and add them to the lists
            x.append(float(x_value))
            y.append(float(y_value))
        except ValueError:
            # Print an error message if the format is invalid
            print(f"Invalid coordinate format: {coordinate}")
            continue
    
    return x, y

# Get the graph title from the user
title = get_title()

# Get the X and Y axis labels from the user
x_label, y_label = get_axis_labels()

# Get the coordinates (X and Y values) from the user
x, y = get_input()

# Check if the number of X and Y values are the same
if len(x) != len(y):
    print("Error: The number of x and y values must be the same.")
else:
    # Set the title and labels for the graph
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Plot the X and Y values on the graph
    plt.plot(x, y)
    
    # Add grid lines to the graph for better readability
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Display the graph
    plt.show()
