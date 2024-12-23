from PIL import Image
import numpy as np

# Function to convert an image to an array
def img_to_array(image_path):
    try:
        # Open the image using PIL
        img = Image.open(image_path)
        
        # Convert the image to a NumPy array
        img_array = np.array(img)
        
        # Display the array shape and return the array
        print(f"Image converted to array with shape: {img_array.shape}")
        return img_array
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Input image path from the user
    image_path = input("Enter the path of the image: ")
    
    # Convert the image to an array
    array = img_to_array(image_path)
    
    # Display the array if needed (optional, as it can be large)
    print(array)
