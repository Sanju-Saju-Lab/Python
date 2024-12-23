import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function for Sobel edge detection
def sobel_edge_detection(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_edge = cv2.magnitude(sobel_x, sobel_y)
    return cv2.normalize(sobel_edge, None, 0, 255, cv2.NORM_MINMAX)

# Function for Prewitt edge detection
def prewitt_edge_detection(image):
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    prewitt_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    prewitt_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    prewitt_edge = cv2.magnitude(prewitt_x, prewitt_y)
    return cv2.normalize(prewitt_edge, None, 0, 255, cv2.NORM_MINMAX)

# Function for Roberts edge detection
def roberts_edge_detection(image):
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    roberts_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    roberts_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    roberts_edge = cv2.magnitude(roberts_x, roberts_y)
    return cv2.normalize(roberts_edge, None, 0, 255, cv2.NORM_MINMAX)

# Function for Canny edge detection
def canny_edge_detection(image):
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 1.4)
    # Apply Canny edge detection
    canny_edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    return canny_edges

# Main function
if __name__ == "__main__":
    # Get the image path from the user
    image_path = input("Enter the path to the image: ").strip()
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Error: Image not found. Please check the path.")
    else:
        # Apply the edge detection techniques
        sobel_edges = sobel_edge_detection(image)
        prewitt_edges = prewitt_edge_detection(image)
        roberts_edges = roberts_edge_detection(image)
        canny_edges = canny_edge_detection(image)
        
        # Display the results using matplotlib
        plt.figure(figsize=(12, 12))
        
        plt.subplot(2, 3, 1)
        plt.imshow(image, cmap='gray')
        plt.title("Original Image")
        plt.axis('off')
        
        plt.subplot(2, 3, 2)
        plt.imshow(sobel_edges, cmap='gray')
        plt.title("Sobel Edge Detection")
        plt.axis('off')
        
        plt.subplot(2, 3, 3)
        plt.imshow(prewitt_edges, cmap='gray')
        plt.title("Prewitt Edge Detection")
        plt.axis('off')
        
        plt.subplot(2, 3, 4)
        plt.imshow(roberts_edges, cmap='gray')
        plt.title("Roberts Edge Detection")
        plt.axis('off')
        
        plt.subplot(2, 3, 5)
        plt.imshow(canny_edges, cmap='gray')
        plt.title("Canny Edge Detection")
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
