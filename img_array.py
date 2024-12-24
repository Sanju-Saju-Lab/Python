from PIL import Image
import numpy as np

# Function to convert an image to an array
def img_to_array(image_path):
    try:
        # Open the image from the given path using PIL (Python Imaging Library)
        img = Image.open(image_path)
        
        # Convert the opened image into a NumPy array (a matrix of pixel values)
        img_array = np.array(img)
        
        # Print the shape of the array (dimensions of the image) and return the array
        print(f"Image converted to array with shape: {img_array.shape}")
        return img_array
    except Exception as e:
        # If there is any error (e.g., file not found), print the error message
        print(f"Error: {e}")

# Main part of the program
if __name__ == "__main__":
    # Ask the user to input the image file path
    image_path = input("Enter the path of the image: ")
    
    # Call the function to convert the image to an array
    array = img_to_array(image_path)
    
    # Print the array to see the pixel values (optional, because it can be large)
    print(array)
