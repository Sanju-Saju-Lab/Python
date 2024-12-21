import matplotlib.pyplot as plt

# Prompt the user to enter the title of the pie chart
title = input("Enter the title of the pie chart: ")

# Function to get the data for the pie chart from the user
def input_pie_chart_data():
    # Ask the user how many categories the pie chart will have
    num_categories = int(input("Enter the number of categories: "))
    
    # Initialize two empty lists: one for the category names and one for their corresponding values
    categories = []
    values = []
    
    # Loop through and ask for each category name and its value
    for i in range(num_categories):
        category = input(f"Enter the name of category {i + 1}: ")
        value = float(input(f"Enter the value for {category}: "))
        
        # Add the category and value to the respective lists
        categories.append(category)
        values.append(value)
    
    # Return the lists of categories and their values
    return categories, values

# Get the data from the function
categories, values = input_pie_chart_data()

# Choose colors for the pie chart slices, using a color map
colors = plt.cm.Paired(range(len(categories)))

# Set the center and radius for the pie chart
x_center = 0
y_center = 0
radius = 1

# Create a new figure and axes for the plot, setting the size of the figure
fig, ax = plt.subplots(figsize=(8, 5))

# Create the pie chart using the input values
# This includes labels, colors, percentage display, and other properties
wedges, texts, autotexts = ax.pie(
    values, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, 
    center=(x_center, y_center), radius=radius
)

# Set the title of the pie chart
ax.set_title(title)

# Create a list of data for the table (category names and their values)
cell_text = [[categories[i], values[i]] for i in range(len(categories))]

# Set the colors for the table rows to match the pie chart colors
table_colors = [[colors[i], colors[i]] for i in range(len(categories))]

# Dynamically adjust the height of the table based on the number of categories
table_height = 0.1 + 0.05 * len(categories)  # Adjust the factor (0.05) to control height expansion

# Create and format the table on the right side of the plot
table = plt.table(
    cellText=cell_text,
    colLabels=["Category", "Values"],
    cellColours=table_colors,
    loc='right',
    cellLoc='center',
    colLoc='center',
    fontsize=12,
    bbox=[1.0, 0.1, 0.4, table_height],  # Adjusted bbox to change height dynamically
)

# Adjust the layout of the plot to fit the pie chart and table nicely
plt.subplots_adjust(left=0.3, right=0.8)

# Display the plot with the pie chart and table
plt.show()
