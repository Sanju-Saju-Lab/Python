# Importing necessary libraries
import matplotlib.pyplot as plt  # For creating the plot
import numpy as np  # For numerical calculations (e.g., angles)

# Function to create the radar chart
def create_radar_chart(categories, data_sets, labels, title):
    # Number of categories in the radar chart
    num_vars = len(categories)

    # Compute angle for each category to distribute them evenly on the radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Complete the loop so the chart looks circular by adding the first angle at the end
    angles += angles[:1]

    # Create a figure and polar axis (for radar chart)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Loop over each dataset and plot it
    for values, label in zip(data_sets, labels):
        # Complete the loop for each dataset by adding the first value at the end
        values += values[:1]
        
        # Plot the dataset on the radar chart
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=label)
        
        # Fill the area under the plot to make it visually clearer
        ax.fill(angles, values, alpha=0.25)

    # Set the labels for the categories (the axes of the radar chart)
    ax.set_xticks(angles[:-1])  # Exclude the last angle because it's a repeat of the first one
    ax.set_xticklabels(categories)  # Label each axis with the corresponding category

    # Add a title to the chart
    ax.set_title(title, size=16, pad=20)

    # Add a legend to show which dataset corresponds to which line
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Show the chart
    plt.show()

# Ask for the title of the chart
title = input("Enter the chart title: ")

# Input: Asking the user to provide categories and datasets
categories = input("Enter the categories separated by commas: ").split(',')
categories = [cat.strip() for cat in categories]  # Remove extra spaces around categories

# Ask for the number of datasets to plot
num_datasets = int(input("Enter the number of datasets: "))
data_sets = []  # This will hold the datasets
labels = []  # This will hold the labels for each dataset

# Collect data for each dataset
for i in range(num_datasets):
    label = input(f"Enter label for dataset {i + 1}: ")  # Ask for a label for the dataset
    labels.append(label)  # Add the label to the labels list
    # Ask for the values for this dataset (separated by commas)
    values = list(map(float, input(f"Enter values for {label} separated by commas: ").split(',')))
    
    # Check if the number of values matches the number of categories
    if len(values) != len(categories):
        print(f"Error: The number of values must match the number of categories for {label}.")
        exit()  # Stop the program if there is an error
    data_sets.append(values)  # Add the dataset to the list of datasets

# Generate the radar chart using the provided data
create_radar_chart(categories, data_sets, labels, title)
