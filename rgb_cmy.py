import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to convert RGB image to CMY
def rgb_to_cmy(image):
    # Normalize the RGB values to the range [0, 1]
    rgb_normalized = image / 255.0
    # Convert RGB to CMY by subtracting RGB values from 1
    cmy_image = 1 - rgb_normalized
    return cmy_image

# Function to convert CMY image back to RGB
def cmy_to_rgb(cmy_image):
    # Convert CMY back to RGB by subtracting CMY values from 1
    rgb_normalized = 1 - cmy_image
    # Scale back the values to the range [0, 255] and convert to uint8 type
    rgb_image = (rgb_normalized * 255).astype(np.uint8)
    return rgb_image

# Prompt the user to enter the path to the input image
input_image_path = input("Enter the path of the image: ")

try:
    # Open the image using Pillow
    input_image = Image.open(input_image_path)
    # Convert the image to RGB and then to a NumPy array
    input_image_rgb = np.array(input_image.convert('RGB'))
    
    # Convert the RGB image to CMY
    cmy_image = rgb_to_cmy(input_image_rgb)
    
    # Convert the CMY image back to RGB
    restored_rgb_image = cmy_to_rgb(cmy_image)

    # Create a figure with three subplots
    plt.figure(figsize=(15, 5))

    # Show the original RGB image
    plt.subplot(1, 3, 1)
    plt.imshow(input_image_rgb)
    plt.title('Original RGB Image')
    plt.axis('off')

    # Show the converted CMY image
    plt.subplot(1, 3, 2)
    plt.imshow(cmy_image)
    plt.title('CMY Image')
    plt.axis('off')

    # Show the restored RGB image
    plt.subplot(1, 3, 3)
    plt.imshow(restored_rgb_image)
    plt.title('Restored RGB Image')
    plt.axis('off')

    # Display the images
    plt.show()

except Exception as e:
    print(f"Error: {e}")
