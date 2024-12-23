import cv2
import matplotlib.pyplot as plt

# Get input from user
image_path = input("Enter the image path: ")

# Read image from disk
img = cv2.imread(image_path)

# Check if image is loaded correctly
if img is None:
    print("Error: Image not found. Please check the path.")
else:
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert RGB image to Grayscale
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    # Plot the original image
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')

    # Plot the grayscale image
    axs[1].imshow(image_gray, cmap='gray')
    axs[1].set_title('Grayscale Image')

    # Remove ticks from the subplots
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Display the subplots
    plt.tight_layout()
    plt.show()
