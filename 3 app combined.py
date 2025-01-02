# import tkinter as tk
# from tkinter import messagebox
# import subprocess
# import os
# import sys
# import Image_Compressor_Project.image_compressor

# # Add the project directory to sys.path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# # Global variable to hold the instance of Complaint Management System
# cms_app = None

# # Define the button actions
# def open_image_compressor():
#     """ Launch the Image Compressor """
#     try:
#         app = Image_Compressor_Project.image_compressor.ImageCompressorApp()
#         if app.select_image():
#             app.compress_image()
#     except Exception as e:
#         messagebox.showerror("Error", f"Could not launch Image Compressor: {str(e)}")

# def open_pdf_encryptor():
#     """ Launch the PDF Locker application """
#     try:
#         pdf_locker_path = os.path.join(os.path.dirname(__file__), "Pdf_Locker", "main.py")
#         subprocess.Popen(["python", pdf_locker_path])
#     except Exception as e:
#         messagebox.showerror("Error", f"Could not launch PDF Locker: {str(e)}")

# def open_complaint_management_system():
#     """ Launch the Complaint Management System for submitting complaints """
#     global cms_app
#     try:
#         if cms_app is not None:
#             cms_app.destroy()  # Destroy previous instance if it exists
        
#         # Import and call the function to run the complaint management system
        
#         cms_app = run_complaint_management_system  # This will create and display the complaint submission form
#     except Exception as e:
#         messagebox.showerror("Error", f"Could not launch Complaint Management: {str(e)}")

# # Create the main window
# root = tk.Tk()
# root.title("Tool Selection")

# # Set the window to full screen
# root.attributes("-fullscreen", True)

# # Create a Canvas for the background
# canvas = tk.Canvas(root, bg="#2E2E2E")  # Dark gray background
# canvas.pack(fill="both", expand=True)

# # Add the title label at the top with larger, bold font
# title_label = tk.Label(canvas, text="All Three Softwares Combined", font=("Helvetica", 48, "bold"), bg="#2E2E2E", fg="white")
# title_label.pack(pady=(20, 0))  # Add some padding to the top

# # Create a frame for better layout control with dark background
# frame = tk.Frame(root, bg="#1C1C1C")  # Darker gray for the frame
# frame.place(relx=0.5, rely=0.5, anchor="center")

# # Create and place the instruction label with larger font
# instruction_label = tk.Label(frame, text="Choose any option", font=("Helvetica", 36), bg="#1C1C1C", fg="white")
# instruction_label.grid(row=0, column=0, columnspan=2, pady=40)

# # Create buttons with larger font and fixed size
# button_color = "#3C3C3C"  # Darker gray for the buttons
# button1 = tk.Button(frame, text="Image Compressor", font=("Helvetica", 20), command=open_image_compressor, height=3, width=20, bg=button_color, fg="white")
# button2 = tk.Button(frame, text="PDF Encryptor", font=("Helvetica", 20), command=open_pdf_encryptor, height=3, width=20, bg=button_color, fg="white")
# button3 = tk.Button(frame, text="Complaint Management System", font=("Helvetica", 20), command=open_complaint_management_system, height=3, width=30, bg=button_color, fg="white")

# # Arrange buttons in a grid
# button1.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
# button2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
# button3.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# # Adjust column weights to ensure buttons expand properly
# frame.columnconfigure(0, weight=1)
# frame.columnconfigure(1, weight=1)

# # Exit fullscreen and hide the window using the Escape key
# def exit_fullscreen(event=None):
#     root.withdraw()  # Hide the window

# root.bind("<Escape>", exit_fullscreen)

# # Start the main event loop
# root.mainloop()



import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
import Image_Compressor_Project.image_compressor
# Add the project directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Global variable to hold the instance of Complaint Management System
cms_app = None

# Define the button actions
def open_image_compressor():
    """ Launch the Image Compressor """
    try:
        app = Image_Compressor_Project.image_compressor.ImageCompressorApp()
        if app.select_image():
            app.compress_image()
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch Image Compressor: {str(e)}")

def open_pdf_encryptor():
    """ Launch the PDF Locker application """
    try:
        pdf_locker_path = os.path.join(os.path.dirname(__file__), "Pdf_Locker", "main.py")
        subprocess.Popen(["python", pdf_locker_path])
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch PDF Locker: {str(e)}")

def open_complaint_management_system():
    """ Launch the Complaint Management System for submitting complaints """
    global cms_app
    try:
        # if cms_app is not None:
        #     cms_app.destroy()  # Destroy previous instance if it exists
        
        # Initialize the Complaint Management System only when the button is clicked
        import complain_management_system  # Import here to prevent automatic invocation

        # Now initialize and launch the Complaint Management System
        cms_app = tk.Tk()  # Create a new root window for the CMS
        cms = complain_management_system.ComplaintManagementSystem()  # Create an instance of the CMS
        app = complain_management_system.ComplaintApp(cms_app, cms)  # Initialize the complaint app

        cms_app.mainloop()  # Start the Tkinter event loop for the complaint management system
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch Complaint Management: {str(e)}")


# Create the main window
root = tk.Tk()
root.title("Tool Selection")

# Set the window to full screen
root.attributes("-fullscreen", True)

# Create a Canvas for the background
canvas = tk.Canvas(root, bg="#2E2E2E")  # Dark gray background
canvas.pack(fill="both", expand=True)

# Add the title label at the top with larger, bold font
title_label = tk.Label(canvas, text="All Three Softwares Combined", font=("Helvetica", 48, "bold"), bg="#2E2E2E", fg="white")
title_label.pack(pady=(20, 0))  # Add some padding to the top

# Create a frame for better layout control with dark background
frame = tk.Frame(root, bg="#1C1C1C")  # Darker gray for the frame
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create and place the instruction label with larger font
instruction_label = tk.Label(frame, text="Choose any option", font=("Helvetica", 36), bg="#1C1C1C", fg="white")
instruction_label.grid(row=0, column=0, columnspan=2, pady=40)

# Create buttons with larger font and fixed size
button_color = "#3C3C3C"  # Darker gray for the buttons
button1 = tk.Button(frame, text="Image Compressor", font=("Helvetica", 20), command=open_image_compressor, height=3, width=20, bg=button_color, fg="white")
button2 = tk.Button(frame, text="PDF Encryptor", font=("Helvetica", 20), command=open_pdf_encryptor, height=3, width=20, bg=button_color, fg="white")
button3 = tk.Button(frame, text="Complaint Management System", font=("Helvetica", 20), command=open_complaint_management_system, height=3, width=30, bg=button_color, fg="white")

# Arrange buttons in a grid
button1.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
button2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
button3.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# Adjust column weights to ensure buttons expand properly
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Exit fullscreen and hide the window using the Escape key
def exit_fullscreen(event=None):
    root.withdraw()  # Hide the window

root.bind("<Escape>", exit_fullscreen)

# Start the main event loop
root.mainloop()
