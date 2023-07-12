'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests
def main():
    # TODO: Add code to test the functions in this module

    #apod_date test function!
    apod_date = '2023-07-12'
    apod_info = get_apod_info(apod_date)
    if apod_info is not None:
        print('Apod information retreievd successfully!')
    else:
        print('Failed to retrieved apod information!')
    
    #apod_image test function
    image_info = get_apod_image_url(apod_info)
    if image_info is not None:
        print('Apod Image retrieved succesfully!')
    else:
        print('Failed to retrieve apod image!')
         

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    # TODO: Complete the function body
    url = "https://api.nasa.gov/planetary/apod"
    # Hint: The APOD API uses query string parameters: https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
    # Hint: Set the 'thumbs' parameter to True so the info returned for video APODs will include URL of the video thumbnail image 
    params = {
        "date": apod_date,
        "thumbs": True,
        "api_key": 'Yv8IEeWphj5LD2AVacydfOF2HchUJrBnSmD4V0BE'
    }

    try:
        response = requests.get(url, params = params)
        if response.ok:
            return response.json()
        else:
            print(f"Falied! Status code: {response.status_code}")
    except requests.RequestException as e:
        print("Error on request:", e)

    return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    # TODO: Complete the function body
    if apod_info_dict['media_type'] == 'image':
        return apod_info_dict['hdurl']
    
    elif apod_info_dict['media_type'] == 'video':
        return apod_info_dict['thumbnail_url']
    else:
        return None
    # Hint: The APOD info dictionary includes a key named 'media_type' that indicates whether the APOD is an image or video
    

if __name__ == '__main__':
    main()