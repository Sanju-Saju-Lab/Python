# Import the necessary Libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Get user input for the image path and translation values
image_path = input("Enter the path of the image: ")
tx = int(input("Enter the horizontal shift (tx): "))
ty = int(input("Enter the vertical shift (ty): "))

# Read the image from the provided path
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print("Error: Unable to load image. Please check the path.")
else:
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    width = image_rgb.shape[1]
    height = image_rgb.shape[0]

    # Translation matrix
    translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
    # Apply the translation
    translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(7, 4))

    # Plot the original image
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')

    # Plot the translated image
    axs[1].imshow(translated_image)
    axs[1].set_title('Translated Image')

    # Remove ticks from the subplots
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Display the subplots
    plt.tight_layout()
    plt.show()
