from PIL import Image
import numpy as np

# Ask the user for the path to the grayscale image
image_path = input("Enter the path of the grayscale image: ")

# Open the grayscale image from the provided path
grayscale_image = Image.open(image_path)

# Convert the grayscale image to a numpy array for processing
grayscale_array = np.array(grayscale_image)

# Convert the single channel grayscale image into 3 identical channels (RGB)
rgb_array = np.stack((grayscale_array, grayscale_array, grayscale_array), axis=-1)

# Convert the numpy array back into an image format
rgb_image = Image.fromarray(rgb_array)

# Ask the user for the path where the new RGB image should be saved
output_path = input("Enter the path to save the RGB image: ")

# Save the RGB image to the specified path
rgb_image.save(output_path)

# Display the newly created RGB image
rgb_image.show()
