# Importing required libraries for image processing and plotting
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Ask the user to input the path of the image and translation values
image_path = input("Enter the path of the image: ")
tx = int(input("Enter the horizontal shift (tx): "))
ty = int(input("Enter the vertical shift (ty): "))

# Load the image from the specified path
img = cv2.imread(image_path)

# Check if the image is loaded correctly
if img is None:
    print("Error: Unable to load image. Please check the path.")
else:
    # Convert the image from BGR (OpenCV's default) to RGB for displaying correctly
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get the width and height of the image
    width = image_rgb.shape[1]
    height = image_rgb.shape[0]

    # Create a translation matrix with the provided horizontal and vertical shifts
    translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)

    # Apply the translation to the image
    translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))

    # Create a subplot with two columns to display both original and translated images
    fig, axs = plt.subplots(1, 2, figsize=(7, 4))

    # Display the original image in the first subplot
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')

    # Display the translated image in the second subplot
    axs[1].imshow(translated_image)
    axs[1].set_title('Translated Image')

    # Remove the axis ticks from both subplots for a cleaner view
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Adjust the layout to ensure the images are displayed neatly
    plt.tight_layout()

    # Show the plot with both images
    plt.show()
