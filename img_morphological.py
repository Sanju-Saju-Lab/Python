# Import the necessary libraries for image processing and plotting
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ask the user to input the path to the image file
image_path = input("Enter the path of the image: ")

# Load the image using OpenCV
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to load.")
    exit()  # Stop the program if the image can't be loaded

# Convert the image from color (BGR) to grayscale for easier processing
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a small square matrix (3x3) for use in image transformations
kernel = np.ones((3, 3), np.uint8)

# Apply dilation to the grayscale image. This makes bright regions grow larger
dilated = cv2.dilate(image_gray, kernel, iterations=2)

# Apply erosion to the grayscale image. This makes bright regions shrink
eroded = cv2.erode(image_gray, kernel, iterations=2)

# Apply opening operation (erosion followed by dilation) to remove noise from the image
opening = cv2.morphologyEx(image_gray, cv2.MORPH_OPEN, kernel)

# Apply closing operation (dilation followed by erosion) to fill small holes in the image
closing = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, kernel)

# Create a 2x2 grid of subplots to display the processed images
fig, axs = plt.subplots(2, 2, figsize=(7, 7))

# Display the dilated image in the first subplot
axs[0,0].imshow(dilated, cmap='Greys')
axs[0,0].set_title('Dilated Image')  # Add title to the plot
axs[0,0].set_xticks([])  # Remove x-axis ticks for cleaner display
axs[0,0].set_yticks([])  # Remove y-axis ticks for cleaner display

# Display the eroded image in the second subplot
axs[0,1].imshow(eroded, cmap='Greys')
axs[0,1].set_title('Eroded Image')
axs[0,1].set_xticks([])
axs[0,1].set_yticks([])

# Display the opening result in the third subplot
axs[1,0].imshow(opening, cmap='Greys')
axs[1,0].set_title('Opening')
axs[1,0].set_xticks([])
axs[1,0].set_yticks([])

# Display the closing result in the fourth subplot
axs[1,1].imshow(closing, cmap='Greys')
axs[1,1].set_title('Closing')
axs[1,1].set_xticks([])
axs[1,1].set_yticks([])

# Adjust layout so that the images are displayed neatly
plt.tight_layout()

# Show the plot with all the subplots
plt.show()
