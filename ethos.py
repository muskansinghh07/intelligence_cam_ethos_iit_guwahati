import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Function to sharpen the image (unsharp masking)
def sharpen_image(image):
    blurred = cv2.GaussianBlur(image, (9, 9), 10.0)
    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
    return sharpened

# Function to resize the image based on user input
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

# Function to display images
def display_images(original, processed):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title('Processed Image')
    plt.imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Function to process the image
def process_image(image_path, width, height, output_folder):
    image = cv2.imread(image_path)
    if image is None:
        messagebox.showerror("Error", "Unable to load image!")
        return
    
    sharpened_image = sharpen_image(image)
    resized_image = resize_image(sharpened_image, width, height)
    
    output_file = os.path.join(output_folder, "processed_image.png")
    cv2.imwrite(output_file, resized_image)
    
    messagebox.showinfo("Success", f"Processed image saved at: {output_file}")
    display_images(image, resized_image)

# Function to select image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        image_path_entry.delete(0, ctk.END)
        image_path_entry.insert(0, file_path)

# Function to select output folder
def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_entry.delete(0, ctk.END)
        output_folder_entry.insert(0, folder_path)

# Function to process button click
def on_process_click():
    image_path = image_path_entry.get()
    output_folder = output_folder_entry.get()
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid dimensions!")
        return
    
    if not image_path or not output_folder:
        messagebox.showerror("Error", "Please select an image and output folder!")
    else:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        process_image(image_path, width, height, output_folder)

# Function to change button color on hover
def on_hover_enter(button):
    button.configure(fg_color="#101010")

def on_hover_leave(button):
    button.configure(fg_color="purple")

# GUI setup using customtkinter
ctk.set_appearance_mode("dark")  # Enable dark mode
ctk.set_default_color_theme("dark-blue")  # Optional: Set color theme

app = ctk.CTk()  # Use CTk() instead of Tk() in customtkinter
app.title("Intelligence Cam")
app.geometry("400x400")

# Image Path Input
image_path_label = ctk.CTkLabel(app, text="Select Image:")
image_path_label.pack(pady=5)
image_path_entry = ctk.CTkEntry(app, width=250)
image_path_entry.pack(pady=5)
select_image_button = ctk.CTkButton(app, text="Browse", command=select_image)
select_image_button.pack(pady=5)

# Output Folder Input
output_folder_label = ctk.CTkLabel(app, text="Select Output Folder:")
output_folder_label.pack(pady=5)
output_folder_entry = ctk.CTkEntry(app, width=250)
output_folder_entry.pack(pady=5)
select_output_button = ctk.CTkButton(app, text="Browse", command=select_output_folder)
select_output_button.pack(pady=5)

# Width and Height Input
width_label = ctk.CTkLabel(app, text="Enter Width:")
width_label.pack(pady=5)
width_entry = ctk.CTkEntry(app, width=100)
width_entry.pack(pady=5)

height_label = ctk.CTkLabel(app, text="Enter Height:")
height_label.pack(pady=5)
height_entry = ctk.CTkEntry(app, width=100)
height_entry.pack(pady=5)

# Process Button
process_button = ctk.CTkButton(app, text="Process Image", command=on_process_click)
process_button.pack(pady=20)

# Start the GUI loop
app.mainloop()
