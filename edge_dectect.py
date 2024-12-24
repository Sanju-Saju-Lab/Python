import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform Sobel edge detection
def sobel_edge_detection(image):
    # Apply Sobel filter in the X and Y directions
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    # Combine the results from both directions
    sobel_edge = cv2.magnitude(sobel_x, sobel_y)
    # Normalize the edge image to have values between 0 and 255
    return cv2.normalize(sobel_edge, None, 0, 255, cv2.NORM_MINMAX)

# Function to perform Prewitt edge detection
def prewitt_edge_detection(image):
    # Define Prewitt kernels for X and Y directions
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    # Apply the kernels using filter2D
    prewitt_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    prewitt_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    # Combine the results from both directions
    prewitt_edge = cv2.magnitude(prewitt_x, prewitt_y)
    # Normalize the edge image to have values between 0 and 255
    return cv2.normalize(prewitt_edge, None, 0, 255, cv2.NORM_MINMAX)

# Function to perform Roberts edge detection
def roberts_edge_detection(image):
    # Define Roberts kernels for X and Y directions
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    # Apply the kernels using filter2D
    roberts_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    roberts_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    # Combine the results from both directions
    roberts_edge = cv2.magnitude(roberts_x, roberts_y)
    # Normalize the edge image to have values between 0 and 255
    return cv2.normalize(roberts_edge, None, 0, 255, cv2.NORM_MINMAX)

# Function to perform Canny edge detection
def canny_edge_detection(image):
    # Apply GaussianBlur to reduce image noise before edge detection
    blurred = cv2.GaussianBlur(image, (5, 5), 1.4)
    # Apply Canny edge detection
    canny_edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    return canny_edges

# Main function to handle the image loading and display
if __name__ == "__main__":
    # Prompt the user for the image file path
    image_path = input("Enter the path to the image: ").strip()
    # Load the image in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Image not found. Please check the path.")
    else:
        # Apply different edge detection techniques
        sobel_edges = sobel_edge_detection(image)
        prewitt_edges = prewitt_edge_detection(image)
        roberts_edges = roberts_edge_detection(image)
        canny_edges = canny_edge_detection(image)
        
        # Display the original and processed images using matplotlib
        plt.figure(figsize=(12, 12))
        
        # Display original image
        plt.subplot(2, 3, 1)
        plt.imshow(image, cmap='gray')
        plt.title("Original Image")
        plt.axis('off')
        
        # Display Sobel edge detection result
        plt.subplot(2, 3, 2)
        plt.imshow(sobel_edges, cmap='gray')
        plt.title("Sobel Edge Detection")
        plt.axis('off')
        
        # Display Prewitt edge detection result
        plt.subplot(2, 3, 3)
        plt.imshow(prewitt_edges, cmap='gray')
        plt.title("Prewitt Edge Detection")
        plt.axis('off')
        
        # Display Roberts edge detection result
        plt.subplot(2, 3, 4)
        plt.imshow(roberts_edges, cmap='gray')
        plt.title("Roberts Edge Detection")
        plt.axis('off')
        
        # Display Canny edge detection result
        plt.subplot(2, 3, 5)
        plt.imshow(canny_edges, cmap='gray')
        plt.title("Canny Edge Detection")
        plt.axis('off')
        
        # Adjust the layout to make it look neat
        plt.tight_layout()
        plt.show()
