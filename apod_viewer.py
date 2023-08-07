from tkinter import *
import apod_desktop
import apod_api
import image_lib

def update_apod():
    apod_date = entry_date.get()  # Get APOD date from user input
    apod_info = apod_api.get_apod_info(apod_date)
    if apod_info is not None:
        image_url = apod_api.get_apod_image_url(apod_info)
        image_data = image_lib.download_image(image_url)
        if image_data is not None:
            apod_image_label.config(image=image_data)
            explanation_text.config(text=apod_info.get('explanation', ''))
        else:
            explanation_text.config(text="Failed to retrieve APOD image!")
    else:
        explanation_text.config(text="Failed to retrieve APOD information!")

# Initialize the image cache
apod_desktop.init_apod_cache()

# TODO: Create the GUI
root = Tk()
root.geometry('800x600')
root.title('NASA APOD Viewer')

entry_date = Entry(root)
entry_date.pack(pady=10)

update_button = Button(root, text="Set as Desktop Image", command=update_apod)
update_button.pack(pady=10)

apod_image_label = Label(root)
apod_image_label.pack(pady=10)

explanation_text = Label(root, wraplength=700, justify=LEFT)
explanation_text.pack(pady=10)


root.mainloop()