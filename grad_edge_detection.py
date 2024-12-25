import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function for Sobel edge detection
def sobel_edge_detection(image):
    # Sobel kernels for detecting edges in X (horizontal) and Y (vertical) directions
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel kernel for horizontal edges
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel kernel for vertical edges
    
    # Calculate the magnitude of the gradient (strength of the edges)
    sobel_edge = cv2.magnitude(sobel_x, sobel_y)
    return sobel_edge

# Function for Prewitt edge detection
def prewitt_edge_detection(image):
    # Prewitt kernels for detecting edges in X and Y directions
    kernel_x = np.array([[ -1, 0, 1], [-1, 0, 1], [-1, 0, 1]])  # Prewitt kernel for horizontal edges
    kernel_y = np.array([[ 1, 1, 1], [ 0, 0, 0], [-1, -1, -1]])  # Prewitt kernel for vertical edges
    
    # Convolve (apply) the kernels to the image to get edges in both directions
    prewitt_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)  # Apply horizontal kernel
    prewitt_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)  # Apply vertical kernel
    
    # Calculate the magnitude of the gradient (strength of the edges)
    prewitt_edge = cv2.magnitude(prewitt_x, prewitt_y)
    return prewitt_edge

# Function for Roberts edge detection
def roberts_edge_detection(image):
    # Roberts kernels for detecting edges in X and Y directions
    kernel_x = np.array([[1, 0], [0, -1]])  # Roberts kernel for horizontal edges
    kernel_y = np.array([[0, 1], [-1, 0]])  # Roberts kernel for vertical edges
    
    # Convolve (apply) the kernels to the image to get edges in both directions
    roberts_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)  # Apply horizontal kernel
    roberts_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)  # Apply vertical kernel
    
    # Calculate the magnitude of the gradient (strength of the edges)
    roberts_edge = cv2.magnitude(roberts_x, roberts_y)
    return roberts_edge

# Input image path from the user
image_path = input("Enter the path to the image: ")

# Read the image and convert it to grayscale (grayscale is simpler for edge detection)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is read successfully
if image is None:
    print("Error: Image not found.")
else:
    # Apply the edge detection methods
    sobel_edges = sobel_edge_detection(image)  # Apply Sobel edge detection
    prewitt_edges = prewitt_edge_detection(image)  # Apply Prewitt edge detection
    roberts_edges = roberts_edge_detection(image)  # Apply Roberts edge detection
    
    # Display the results using matplotlib
    plt.figure(figsize=(10, 10))
    
    # Show the original image
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')  # Show image in grayscale
    plt.title("Original Image")
    plt.axis('off')  # Hide axes
    
    # Show Sobel edge detection result
    plt.subplot(2, 2, 2)
    plt.imshow(sobel_edges, cmap='gray')  # Show Sobel edges
    plt.title("Sobel Edge Detection")
    plt.axis('off')  # Hide axes
    
    # Show Prewitt edge detection result
    plt.subplot(2, 2, 3)
    plt.imshow(prewitt_edges, cmap='gray')  # Show Prewitt edges
    plt.title("Prewitt Edge Detection")
    plt.axis('off')  # Hide axes
    
    # Show Roberts edge detection result
    plt.subplot(2, 2, 4)
    plt.imshow(roberts_edges, cmap='gray')  # Show Roberts edges
    plt.title("Roberts Edge Detection")
    plt.axis('off')  # Hide axes
    
    plt.tight_layout()  # Adjust the layout for better display
    plt.show()  # Display all images
