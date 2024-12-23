# Import the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to get valid numeric input
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

# Get the image path from the user
image_path = input("Enter the path of the image: ")

# Get valid scale factors from the user
scale_factor_1 = get_valid_input("Enter the zoom-in scale factor: ")
scale_factor_2 = get_valid_input("Enter the scale-down factor: ")

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error loading the image. Please check the file path.")
else:
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get the original image dimensions
    height, width = image_rgb.shape[:2]

    # Calculate the new image dimensions for zooming in
    new_height = int(height * scale_factor_1)
    new_width = int(width * scale_factor_1)

    # Resize the image (zooming in)
    zoomed_image = cv2.resize(src=image_rgb, 
                              dsize=(new_width, new_height), 
                              interpolation=cv2.INTER_CUBIC)

    # Calculate the new image dimensions for scaling down
    new_height1 = int(height * scale_factor_2)
    new_width1 = int(width * scale_factor_2)

    # Resize the image (scaling down)
    scaled_image = cv2.resize(src=image_rgb, 
                              dsize=(new_width1, new_height1), 
                              interpolation=cv2.INTER_AREA)

    # Create subplots to display the images
    fig, axs = plt.subplots(1, 3, figsize=(10, 4))

    # Plot the original image
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image Shape:' + str(image_rgb.shape))

    # Plot the Zoomed Image
    axs[1].imshow(zoomed_image)
    axs[1].set_title('Zoomed Image Shape:' + str(zoomed_image.shape))

    # Plot the Scaled Image
    axs[2].imshow(scaled_image)
    axs[2].set_title('Scaled Image Shape:' + str(scaled_image.shape))

    # Remove ticks from the subplots
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Display the subplots
    plt.tight_layout()
    plt.show()
