from PIL import Image

# Function to resize image
def resize_image(img_path, height, width, save_path):
    # Open an image file
    with Image.open(img_path) as img:
        # Resize image
        resized_img = img.resize((width, height))
        
        # Save the resized image
        resized_img.save(save_path)
        print(f"Image resized to {width}x{height} and saved at '{save_path}'")

# User input
img_path = input("Enter the image path: ")
height, width = map(int, input("Enter the desired height and width: ").split('x'))
save_path = input("Enter the path to save the resized image: ")

# Resize the image
resize_image(img_path, height, width, save_path)
