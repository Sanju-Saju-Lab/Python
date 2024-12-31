import matplotlib.pyplot as plt  # Import the library for creating plots

def create_line_chart():
    print("Line Chart Creator")  # Display the purpose of the program
    
    # Ask the user for the chart title
    chart_title = input("Enter the title of the chart: ")
    
    # Ask how many lines the user wants to plot
    num_lines = int(input("Enter the number of lines you want to plot: "))
    
    data = {}  # Initialize an empty dictionary to store data for each line

    # Loop to collect data for each line
    for i in range(num_lines):
        # Get the label (name) for the line
        label = input(f"Enter the label for line {i+1}: ")
        
        # Get the x-values for the line, separated by spaces
        print(f"Enter the x-values for {label}:")
        x_values = list(map(float, input().split()))  # Convert input to a list of numbers
        
        # Get the y-values for the line, separated by spaces
        print(f"Enter the y-values for {label}:")
        y_values = list(map(float, input().split()))  # Convert input to a list of numbers
        
        # Check if the number of x-values matches the number of y-values
        if len(x_values) != len(y_values):
            print(f"Error: The number of x and y values must match for {label}. Please try again.")
            return  # Exit the program if there is an error
        
        # Save the data for the current line
        data[label] = (x_values, y_values)

    # Plot the data for each line
    for label, (x, y) in data.items():
        plt.plot(x, y, label=label)  # Create a line for the given x and y values

    # Add title, labels, legend, and grid to the chart
    plt.title(chart_title)  # Set the chart title
    plt.xlabel("X-axis")  # Label for the x-axis
    plt.ylabel("Y-axis")  # Label for the y-axis
    plt.legend()  # Add a legend to show labels for each line
    plt.grid(True)  # Add a grid to the background for better readability

    # Display the chart to the user
    plt.show()

# Run the program
create_line_chart()
