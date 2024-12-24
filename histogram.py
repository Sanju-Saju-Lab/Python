import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to plot the histogram for a grayscale image
def plot_histogram_grayscale(image):
    # Calculate the histogram for grayscale image (pixel intensity vs frequency)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display the grayscale image on the first subplot
    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('Grayscale Image')  # Set title
    axs[0].axis('off')  # Turn off axis labels
    
    # Plot the histogram on the second subplot
    axs[1].plot(hist, color='black')
    axs[1].set_title('Grayscale Histogram')  # Set title
    axs[1].set_xlabel('Pixel Intensity')  # Label for X-axis
    axs[1].set_ylabel('Frequency')  # Label for Y-axis
    axs[1].set_xlim([0, 256])  # Set the range for the X-axis
    
    # Adjust layout for better spacing and display the plots
    plt.tight_layout()
    plt.show()

# Function to plot the histogram for a color image
def plot_histogram_color(image):
    # Split the image into three channels (blue, green, red)
    (blue, green, red) = cv2.split(image)
    
    # Calculate histograms for each color channel (red, green, blue)
    hist_red = cv2.calcHist([red], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([green], [0], None, [256], [0, 256])
    hist_blue = cv2.calcHist([blue], [0], None, [256], [0, 256])
    
    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display the color image on the first subplot (convert to RGB for correct colors)
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Color Image')  # Set title
    axs[0].axis('off')  # Turn off axis labels
    
    # Plot histograms for each color channel on the second subplot
    axs[1].plot(hist_red, color='red', label='Red Channel')
    axs[1].plot(hist_green, color='green', label='Green Channel')
    axs[1].plot(hist_blue, color='blue', label='Blue Channel')
    
    # Set titles and labels for the second subplot
    axs[1].set_title('Color Histogram (RGB)')
    axs[1].set_xlabel('Pixel Intensity')
    axs[1].set_ylabel('Frequency')
    axs[1].set_xlim([0, 256])  # Set the range for the X-axis
    
    # Add a legend to the histogram
    axs[1].legend()
    
    # Adjust layout for better spacing and display the plots
    plt.tight_layout()
    plt.show()

# Get the image path from the user
image_path = input("Enter the path of the image: ")

# Read the grayscale version of the image
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Read the color version of the image
color_image = cv2.imread(image_path)

# Check if the images are loaded successfully
if grayscale_image is None or color_image is None:
    print("Error loading image(s). Please check the file paths.")
else:
    # If both images are loaded, plot the histograms for both grayscale and color images
    plot_histogram_grayscale(grayscale_image)
    plot_histogram_color(color_image)
