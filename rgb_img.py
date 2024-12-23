from PIL import Image
import numpy as np

# Input the path of the grayscale image
image_path = input("Enter the path of the grayscale image: ")

# Open the grayscale image
grayscale_image = Image.open(image_path)

# Convert the image to numpy array
grayscale_array = np.array(grayscale_image)

# Stack the grayscale values into 3 channels (R, G, B)
rgb_array = np.stack((grayscale_array, grayscale_array, grayscale_array), axis=-1)

# Convert back to an image
rgb_image = Image.fromarray(rgb_array)

# Save or display the RGB image
output_path = input("Enter the path to save the RGB image: ")
rgb_image.save(output_path)
rgb_image.show()
