import cv2
import matplotlib.pyplot as plt

# Get input from user
image_path = input("Enter the image path: ")

# Input validation for degree of rotation
while True:
    try:
        degree_of_rotation = float(input("Enter the degree of rotation (0-360): "))
        if 0 <= degree_of_rotation <= 360:
            break  # Exit the loop if the input is valid
        else:
            print("Error: Please enter a value between 0 and 360.")
    except ValueError:
        print("Error: Please enter a valid numeric value.")

# Read image from disk
img = cv2.imread(image_path)

# Check if image is loaded correctly
if img is None:
    print("Error: Image not found. Please check the path.")
else:
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Image rotation parameter
    center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
    angle = degree_of_rotation
    scale = 1

    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Perform the rotation
    rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(7, 4))

    # Plot the original image
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')

    # Plot the rotated image
    axs[1].imshow(rotated_image)
    axs[1].set_title(f'Rotated Image ({degree_of_rotation}°)')

    # Remove ticks from the subplots
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Display the subplots
    plt.tight_layout()
    plt.show()
