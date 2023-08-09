'''
Library of useful functions for working with images.
'''
import requests
import platform
import ctypes
import hashlib
from PIL import Image
import io
import os


def main():


    #for testing download image function
    image_url = 'https://apod.nasa.gov/apod/image/2307/Ngc1398_Hanson_2752.jpg'
    image_data = download_image(image_url)
    if image_data is not None:
        print('Image retrieved successfully!')
    else:
        print('Failed to retrieve image!')
    
    #for testing save image function
    image_filename = image_url.split('/')[-1]  # Extract the filename from the URL
    image_file_path = os.path.join(r"C:\Users\16476\Documents\Scripting Applications\Final_Project\images", image_filename)
    saved = save_image_file(image_data, image_file_path)
    if saved:
        print("Image saved successfully!")
    else:
        print("Couldn't save image!")

    #for testing background function
    print("Setting desktop background...")
    saved_in_background = set_desktop_background_image(image_file_path)
    if saved_in_background:
        print("Desktop background changed successfully!")
    else:
        print("Couldn't set the desktop background image!")


def download_image(image_url):
    """Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): URL of image

    Returns:
        bytes: Binary image data, if succcessful. None, if unsuccessful.
    """
    # TODO: Complete function body
    try:
        response = requests.get(image_url)
        if response.ok:
            return response.content
        else:
            print('Please try again!')
    #Catching exceptions too - learnt this from youtube
    except requests.RequestException as e:
        print('Error Occurred:', e)
            
    return None

def save_image_file(image_data, image_path):
    """Saves image data as a file on disk.
    
    DOES NOT DOWNLOAD THE IMAGE.

    Args:
        image_data (bytes): Binary image data
        image_path (str)po: Path to save image file

    Returns:
        bool: True, if succcessful. False, if unsuccessful
    """
    # TODO: Complete function body
    try:
        with Image.open(io.BytesIO(image_data)) as img:
            img.save(image_path)
        return True
    except Exception as e:
        print("Error: Couldn't save image", e)
        return False


def set_desktop_background_image(image_path):
    """Sets the desktop background image to a specific image.

    Args:
        image_path (str): Path of image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful        
    """
    # TODO: Complete function body
    try:
        print("Setting desktop background image:", image_path)
        if platform.system() == 'Windows':
            # Windows-specific code to set desktop background
            
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path.encode('utf-16'), 3)
            return True
        else:
            print("Unsupported platform for setting desktop background!")
            return False
    except Exception as e:
        print("Error: Couldn't set desktop background", e)
        return False
    
def calculate_image_sha256(image_data):
    """Calculates the SHA-256 hash of image data.

    Args:
        image_data (bytes): Binary image data

    Returns:
        str: SHA-256 hash value
    """
    try:
        sha256_hash = hashlib.sha256(image_data).hexdigest()
        return sha256_hash
    except Exception as e:
        print("Error: Couldn't calculate image SHA-256 hash", e)
        return None
    

def scale_image(image_size, max_size=(1200, 1200)):
    """Calculates the dimensions of an image scaled to a maximum width
    and/or height while maintaining the aspect ratio  

    Args:
        image_size (tuple[int, int]): Original image size in pixels (width, height) 
        max_size (tuple[int, int], optional): Maximum image size in pixels (width, height). Defaults to (800, 600).

    Returns:
        tuple[int, int]: Scaled image size in pixels (width, height)
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    # NOTE: This function is only needed to support the APOD viewer GUI
    resize_ratio = min(max_size[0] / image_size[0], max_size[1] / image_size[1])
    new_size = (int(image_size[0] * resize_ratio), int(image_size[1] * resize_ratio))
    return new_size

if __name__ == '__main__':
    main()