from PIL import Image

# Function to resize an image to a specified height and width
def resize_image(img_path, height, width, save_path):
    # Open the image file from the given path
    with Image.open(img_path) as img:
        # Resize the image to the specified dimensions (height and width)
        resized_img = img.resize((width, height))
        
        # Save the resized image to the specified save path
        resized_img.save(save_path)
        # Print a message indicating the image has been resized and saved
        print(f"Image resized to {width}x{height} and saved at '{save_path}'")

# Ask the user for the image path (where the image is located)
img_path = input("Enter the image path: ")

# Ask the user to enter the desired height and width, separated by 'x'
height, width = map(int, input("Enter the desired height and width (e.g., 800x600): ").split('x'))

# Ask the user for the path where the resized image should be saved
save_path = input("Enter the path to save the resized image: ")

# Call the function to resize the image
resize_image(img_path, height, width, save_path)
