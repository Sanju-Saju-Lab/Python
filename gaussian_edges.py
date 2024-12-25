import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform Gaussian smoothing (blur)
def gaussian_blur(image, kernel_size=5, sigma=1):
    # Apply a Gaussian blur to smooth the image and reduce noise
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

# Function for Canny edge detection
def canny_edge_detection(image):
    # Apply Gaussian blur to reduce noise
    blurred_image = gaussian_blur(image)
    # Perform Canny edge detection on the blurred image
    edges = cv2.Canny(blurred_image, 100, 200)
    return edges

# Function for Laplacian of Gaussian (LoG) edge detection
def log_edge_detection(image):
    # Apply Gaussian blur to smooth the image
    blurred_image = gaussian_blur(image)
    # Apply the Laplacian operator to detect edges in the blurred image
    log_edges = cv2.Laplacian(blurred_image, cv2.CV_64F)
    # Convert the result to an absolute scale to make it visible
    log_edges = cv2.convertScaleAbs(log_edges)
    return log_edges

# User input for the image path
image_path = input("Enter the path of the image: ")

# Load the image in grayscale (black and white)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found. Please check the path.")
else:
    # Get the Canny edge detection result
    canny_edges = canny_edge_detection(image)

    # Get the Laplacian of Gaussian (LoG) edge detection result
    log_edges = log_edge_detection(image)

    # Display the images using matplotlib
    plt.figure(figsize=(12, 6))

    # Original Image
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')  # Hide axes

    # Canny edge detection result
    plt.subplot(1, 3, 2)
    plt.imshow(canny_edges, cmap='gray')
    plt.title('Canny Edge Detection')
    plt.axis('off')  # Hide axes

    # Laplacian of Gaussian (LoG) edge detection result
    plt.subplot(1, 3, 3)
    plt.imshow(log_edges, cmap='gray')
    plt.title('Laplacian of Gaussian (LoG)')
    plt.axis('off')  # Hide axes

    # Adjust the layout and display all images
    plt.tight_layout()
    plt.show()
