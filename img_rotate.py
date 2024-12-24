import cv2
import matplotlib.pyplot as plt

# Ask the user to input the path of the image they want to rotate
image_path = input("Enter the image path: ")

# Loop to get valid input for the degree of rotation
while True:
    try:
        # Ask the user to input the degree of rotation
        degree_of_rotation = float(input("Enter the degree of rotation (0-360): "))
        
        # Check if the input is within the valid range (0-360 degrees)
        if 0 <= degree_of_rotation <= 360:
            break  # Exit the loop if the input is valid
        else:
            print("Error: Please enter a value between 0 and 360.")
    except ValueError:
        # If the input is not a valid number, print an error message
        print("Error: Please enter a valid numeric value.")

# Read the image from the specified path
img = cv2.imread(image_path)

# Check if the image is loaded successfully
if img is None:
    print("Error: Image not found. Please check the path.")
else:
    # Convert the image from BGR (OpenCV default) to RGB (for display with matplotlib)
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Calculate the center of the image for rotation
    center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
    angle = degree_of_rotation  # The degree of rotation input by the user
    scale = 1  # Keep the scale as 1 (no resizing during rotation)

    # Get the matrix that will be used for rotating the image
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Apply the rotation to the image using the rotation matrix
    rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))

    # Create a subplot with two images: original and rotated
    fig, axs = plt.subplots(1, 2, figsize=(7, 4))

    # Display the original image on the first subplot
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')

    # Display the rotated image on the second subplot
    axs[1].imshow(rotated_image)
    axs[1].set_title(f'Rotated Image ({degree_of_rotation}°)')

    # Remove x and y ticks from both subplots for better presentation
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Automatically adjust the layout of the subplots
    plt.tight_layout()
    
    # Show the plot with the images
    plt.show()
