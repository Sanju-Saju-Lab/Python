import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_grayscale(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('Grayscale Image')
    axs[0].axis('off')
    axs[1].plot(hist, color='black')
    axs[1].set_title('Grayscale Histogram')
    axs[1].set_xlabel('Pixel Intensity')
    axs[1].set_ylabel('Frequency')
    axs[1].set_xlim([0, 256])
    plt.tight_layout()
    plt.show()

def plot_histogram_color(image):
    (blue, green, red) = cv2.split(image)
    hist_red = cv2.calcHist([red], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([green], [0], None, [256], [0, 256])
    hist_blue = cv2.calcHist([blue], [0], None, [256], [0, 256])
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Color Image')
    axs[0].axis('off')
    axs[1].plot(hist_red, color='red', label='Red Channel')
    axs[1].plot(hist_green, color='green', label='Green Channel')
    axs[1].plot(hist_blue, color='blue', label='Blue Channel')
    axs[1].set_title('Color Histogram (RGB)')
    axs[1].set_xlabel('Pixel Intensity')
    axs[1].set_ylabel('Frequency')
    axs[1].set_xlim([0, 256])
    axs[1].legend()
    plt.tight_layout()
    plt.show()

image_path = input("Enter the path of the image: ")
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread(image_path)

if grayscale_image is None or color_image is None:
    print("Error loading image(s). Please check the file paths.")
else:
    plot_histogram_grayscale(grayscale_image)
    plot_histogram_color(color_image)
