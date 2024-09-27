# Intelligence Cam

*Intelligence Cam* is a Python-based GUI application that allows users to apply basic image processing techniques like sharpening and resizing. The user can select an image, specify the desired width and height, and save the processed image to a chosen directory. The application is built using customtkinter for a modern-looking graphical user interface.

## Features

- *Image Selection*: Users can browse and select an image file (.jpg, .png, .jpeg).
- *Image Processing*:
  - *Sharpening*: Applies unsharp masking to enhance the image clarity.
  - *Resizing*: Resize the image based on user-provided width and height.
- *Processed Image Display*: The application displays both the original and processed images side by side.
- *Save Processed Image*: Users can select a directory to save the processed image (processed_image.png).
- *Interactive GUI*: Built using customtkinter, featuring hover effects and a sleek dark mode interface.

## Installation

1. Clone the repository:

   bash
   git clone https://github.com/muskansinghh07/intelligence_cam_ethos_iit_guwahati.git
   cd intelligence-cam
   

2. Install the required dependencies:

   bash
   pip install -r requirements.txt
   

   Or install the dependencies manually:

   bash
   pip install opencv-python matplotlib customtkinter
   

3. Run the application:

   bash
   python intelligence_cam.py
   

## How to Use

1. *Select an Image*: Click the "Browse" button under "Select Image" and choose an image from your system.
2. *Select Output Folder*: Click the "Browse" button under "Select Output Folder" and choose a folder to save the processed image.
3. *Specify Dimensions*: Enter the desired width and height for the resized image.
4. *Process Image*: Click the "Process Image" button to apply sharpening and resizing to the selected image. The processed image will be saved in the specified output folder.
5. *View Output*: After processing, a side-by-side comparison of the original and processed images will be displayed.

## Dependencies

- opencv-python - For image processing functions.
- matplotlib - To display the original and processed images.
- customtkinter - For the modern, customizable GUI.
- tkinter - For file and folder selection dialogs.

## Customization

- *Change Appearance Mode*: The appearance mode is set to "dark". You can switch to light mode by changing the line in the code:
  python
  ctk.set_appearance_mode("light")
  

- *Color Theme*: The color theme is set to "dark-blue". You can choose other available themes or customize your own theme in the GUI by changing:
  python
  ctk.set_default_color_theme("dark-blue")

  ##ScreenShots
  ![image](https://github.com/user-attachments/assets/5ac9048e-15db-45d6-893d-a7d0b24698da)

