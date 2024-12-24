import matplotlib.pyplot as plt

# Ask the user to input the title for the pie chart
title = input("Enter the title of the pie chart: ")

# Function to collect data for the pie chart from the user
def input_pie_chart_data():
    # Ask how many categories the pie chart should have
    num_categories = int(input("Enter the number of categories: "))
    
    # Create two empty lists to store category names and their corresponding values
    categories = []
    values = []
    
    # Loop through and ask for each category name and its value
    for i in range(num_categories):
        category = input(f"Enter the name of category {i + 1}: ")
        value = float(input(f"Enter the value for {category}: "))
        
        # Add the category and value to the lists
        categories.append(category)
        values.append(value)
    
    # Return the lists containing the categories and their values
    return categories, values

# Get the categories and values by calling the function
categories, values = input_pie_chart_data()

# Choose colors for the pie chart slices based on the number of categories
colors = plt.cm.Paired(range(len(categories)))

# Define the center and radius of the pie chart
x_center = 0
y_center = 0
radius = 1

# Create a figure and axes for the pie chart
fig, ax = plt.subplots(figsize=(8, 5))

# Create the pie chart with the data and customize it
# This includes adding labels, percentages, and choosing start angle and colors
wedges, texts, autotexts = ax.pie(
    values, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, 
    center=(x_center, y_center), radius=radius
)

# Set the title for the pie chart
ax.set_title(title)

# Create the data for the table, including categories and their values
cell_text = [[categories[i], values[i]] for i in range(len(categories))]

# Set the colors of the table rows to match the pie chart slices
table_colors = [[colors[i], colors[i]] for i in range(len(categories))]

# Dynamically adjust the height of the table based on the number of categories
table_height = 0.1 + 0.05 * len(categories)  # Adjust height as categories increase

# Add the table to the plot, placing it to the right of the pie chart
table = plt.table(
    cellText=cell_text,
    colLabels=["Category", "Values"],
    cellColours=table_colors,
    loc='right',
    cellLoc='center',
    colLoc='center',
    fontsize=12,
    bbox=[1.0, 0.1, 0.4, table_height],  # Adjust the table size dynamically
)

# Adjust the layout of the plot to fit both the pie chart and the table
plt.subplots_adjust(left=0.3, right=0.8)

# Display the pie chart along with the table
plt.show()
