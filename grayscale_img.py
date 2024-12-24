import cv2
import matplotlib.pyplot as plt

# Ask the user to enter the path of the image
image_path = input("Enter the image path: ")

# Read the image from the given path
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print("Error: Image not found. Please check the path.")
else:
    # Convert the image from BGR (default in OpenCV) to RGB
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert the RGB image to Grayscale
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    # Create a figure with 2 subplots (1 row and 2 columns)
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    # Display the original image on the first subplot
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')

    # Display the grayscale image on the second subplot
    axs[1].imshow(image_gray, cmap='gray')
    axs[1].set_title('Grayscale Image')

    # Remove the x and y ticks for a cleaner display
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Adjust the layout and show the images
    plt.tight_layout()
    plt.show()
