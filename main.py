# import os
# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox
# from PyPDF2 import PdfWriter, PdfReader

# # Create the main window
# root = Tk()
# root.title("Pdf Protector")

# # Set fullscreen mode
# fullscreen = True
# root.attributes("-fullscreen", fullscreen)

# # Absolute path to the icon and top banner image
# icon_path = r"Pdf_Locker\images\application_top_icon.png"
# banner_path = r"Pdf_Locker\images\top_banner.png"

# # Check if the image exists and set it as the icon
# if os.path.exists(icon_path):
#     image_icon = PhotoImage(file=icon_path)
#     root.iconphoto(False, image_icon)
# else:
#     print(f"Icon image not found: {icon_path}")

# # Variables for the form
# source = StringVar()
# target = StringVar()
# password = StringVar()
# check_var = BooleanVar()  # Define check_var for toggling password visibility

# # Input fields need to be defined here globally
# entry1 = None
# entry2 = None
# entry3 = None

# # Function to browse the source PDF file
# def browse_source():
#     global filename
#     filename = filedialog.askopenfilename(initialdir=os.getcwd(),
#                                           title="Select Source PDF File",
#                                           filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
#     entry1.insert(END, filename)

# # Function to browse the target PDF file
# def browse_target():
#     global target_filename
#     target_filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
#                                                    title="Select Target PDF File",
#                                                    defaultextension=".pdf",
#                                                    filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
#     entry2.insert(END, target_filename)

# # Function to protect the PDF with a password
# def Protect():
#     mainfile = source.get()
#     protectfile = target.get()
#     code = password.get()

#     if mainfile == "" and protectfile == "" and password.get() == "":
#         messagebox.showerror("Invalid", "All entries are empty!")
#     elif mainfile == "":
#         messagebox.showerror("Invalid", "Please type the source PDF filename.")
#     elif protectfile == "":
#         messagebox.showerror("Invalid", "Please type the target PDF filename!")
#     elif password.get() == "":
#         messagebox.showerror("Invalid", "Please type a password.")
#     else:
#         try:
#             out = PdfWriter()
#             file = PdfReader(mainfile)
#             num = len(file.pages)

#             for idx in range(num):
#                 page = file.pages[idx]
#                 out.add_page(page)

#             # Password
#             out.encrypt(code)

#             with open(protectfile, "wb") as f:
#                 out.write(f)

#             messagebox.showinfo("Success", "PDF protected successfully!")

#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {str(e)}")

# # Toggle to show or hide password
# def toggle_password():
#     if check_var.get():
#         entry3.config(show='')
#     else:
#         entry3.config(show='*')

# # Function to exit the application
# def exit_application():
#     root.destroy()  # Close the application

# # Override the close button behavior
# root.protocol("WM_DELETE_WINDOW", exit_application)

# # Bind F11 for fullscreen toggle and Esc for exit
# root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
# root.bind("<Escape>", exit_application)

# # Load and display the top banner image if it exists
# if os.path.exists(banner_path):
#     Top_image = PhotoImage(file=banner_path)
#     Label(root, image=Top_image).pack(fill=X)
# else:
#     print(f"Top banner image not found: {banner_path}")

# # Frame for the form
# frame = Frame(root, bd=5, relief=GROOVE, bg='darkgray')  # Set the frame background color
# frame.place(relx=0.01, rely=0.35, relwidth=0.98, relheight=0.6)

# # Adjust the layout of the form
# def adjust_layout():
#     global entry1, entry2, entry3  # Declare these as global so they can be used throughout the code
    
#     # Clear previous layout
#     for widget in frame.winfo_children():
#         widget.grid_forget()

#     # Configure grid columns to expand
#     frame.grid_columnconfigure(0, weight=1)  # Label column
#     frame.grid_columnconfigure(1, weight=5)  # Entry column

#     # Source PDF File Location Section
#     Label(frame, text="Source PDF File Location:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=0, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
#     entry1 = Entry(frame, textvariable=source, font="arial 16", bd=1, width=70)  # Increased font size and widened input box
#     entry1.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

#     Button(frame, text="Select PDF", width=12, bg="#d3cdcd", command=browse_source).grid(row=1, column=1, padx=10, pady=(5, 15), sticky='e')

#     # Target PDF File Name Section
#     Label(frame, text="Target PDF File Name:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=2, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
#     entry2 = Entry(frame, textvariable=target, font="arial 16", bd=1, width=70)  # Increased font size and widened input box
#     entry2.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

#     # Write User Password Section
#     Label(frame, text="Write User Password:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=3, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
#     entry3 = Entry(frame, textvariable=password, font="arial 16", bd=1, width=70, show='*')  # Increased font size and widened input box
#     entry3.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

#     # Checkbox to show or hide password
#     check_button = Checkbutton(frame, text="Show Password", variable=check_var, onvalue=True, offvalue=False, command=toggle_password, font="arial 16", bg='darkgray', fg="white")  # Updated colors
#     check_button.grid(row=4, column=1, pady=5, sticky='w')

#     # Button to protect the PDF file
#     Protect_button = Button(root, text="Protect PDF File", compound=LEFT, width=20, height=1, bg="#bfb9b9", font="arial 16 bold", command=Protect)  # Increased font size
#     Protect_button.pack(side=BOTTOM, pady=25)

# # Call the layout adjustment function
# adjust_layout()

# # Set the main window's background color
# root.configure(bg='darkgray')  # Set the background color of the root window

# # Start the Tkinter mainloop
# root.mainloop()







# import os
# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox
# from PyPDF2 import PdfWriter, PdfReader

# def create_pdf_locker():
#     # Create the main window
#     root = Tk()
#     root.title("Pdf Protector")

#     # Set fullscreen mode
#     fullscreen = True
#     root.attributes("-fullscreen", fullscreen)

#     # Absolute path to the icon and top banner image
#     icon_path = r"Pdf_Locker\images\application_top_icon.png"
#     banner_path = r"Pdf_Locker\images\top_banner.png"

#     # Check if the image exists and set it as the icon
#     if os.path.exists(icon_path):
#         image_icon = PhotoImage(file=icon_path)
#         root.iconphoto(False, image_icon)
#     else:
#         print(f"Icon image not found: {icon_path}")

#     # Variables for the form
#     source = StringVar()
#     target = StringVar()
#     password = StringVar()
#     check_var = BooleanVar()  # Define check_var for toggling password visibility

#     # Input fields need to be defined here globally
#     entry1 = None
#     entry2 = None
#     entry3 = None

#     # Function to browse the source PDF file
#     def browse_source():
#         global filename
#         filename = filedialog.askopenfilename(initialdir=os.getcwd(),
#                                               title="Select Source PDF File",
#                                               filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
#         entry1.insert(END, filename)

#     # Function to browse the target PDF file
#     def browse_target():
#         global target_filename
#         target_filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
#                                                        title="Select Target PDF File",
#                                                        defaultextension=".pdf",
#                                                        filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
#         entry2.insert(END, target_filename)

#     # Function to protect the PDF with a password
#     def Protect():
#         mainfile = source.get()
#         protectfile = target.get()
#         code = password.get()

#         if mainfile == "" and protectfile == "" and password.get() == "":
#             messagebox.showerror("Invalid", "All entries are empty!")
#         elif mainfile == "":
#             messagebox.showerror("Invalid", "Please type the source PDF filename.")
#         elif protectfile == "":
#             messagebox.showerror("Invalid", "Please type the target PDF filename!")
#         elif password.get() == "":
#             messagebox.showerror("Invalid", "Please type a password.")
#         else:
#             try:
#                 out = PdfWriter()
#                 file = PdfReader(mainfile)
#                 num = len(file.pages)

#                 for idx in range(num):
#                     page = file.pages[idx]
#                     out.add_page(page)

#                 # Password
#                 out.encrypt(code)

#                 with open(protectfile, "wb") as f:
#                     out.write(f)

#                 messagebox.showinfo("Success", "PDF protected successfully!")

#             except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred: {str(e)}")

#     # Toggle to show or hide password
#     def toggle_password():
#         if check_var.get():
#             entry3.config(show='')
#         else:
#             entry3.config(show='*')

#     # Function to exit the application
#     def exit_application():
#         root.destroy()  # Close the application

#     # Override the close button behavior
#     root.protocol("WM_DELETE_WINDOW", exit_application)

#     # Bind F11 for fullscreen toggle and Esc for exit
#     root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
#     root.bind("<Escape>", exit_application)

#     # Load and display the top banner image if it exists
#     if os.path.exists(banner_path):
#         Top_image = PhotoImage(file=banner_path)
#         Label(root, image=Top_image).pack(fill=X)
#     else:
#         print(f"Top banner image not found: {banner_path}")

#     # Frame for the form
#     frame = Frame(root, bd=5, relief=GROOVE, bg='darkgray')  # Set the frame background color
#     frame.place(relx=0.01, rely=0.35, relwidth=0.98, relheight=0.6)

#     # Adjust the layout of the form
#     def adjust_layout():
#         global entry1, entry2, entry3  # Declare these as global so they can be used throughout the code
        
#         # Clear previous layout
#         for widget in frame.winfo_children():
#             widget.grid_forget()

#         # Configure grid columns to expand
#         frame.grid_columnconfigure(0, weight=1)  # Label column
#         frame.grid_columnconfigure(1, weight=5)  # Entry column

#         # Source PDF File Location Section
#         Label(frame, text="Source PDF File Location:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=0, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
#         entry1 = Entry(frame, textvariable=source, font="arial 16", bd=1, width=70)  # Increased font size and widened input box
#         entry1.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

#         Button(frame, text="Select PDF", width=12, bg="#d3cdcd", command=browse_source).grid(row=1, column=1, padx=10, pady=(5, 15), sticky='e')

#         # Target PDF File Name Section
#         Label(frame, text="Target PDF File Name:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=2, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
#         entry2 = Entry(frame, textvariable=target, font="arial 16", bd=1, width=70)  # Increased font size and widened input box
#         entry2.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

#         # Write User Password Section
#         Label(frame, text="Write User Password:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=3, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
#         entry3 = Entry(frame, textvariable=password, font="arial 16", bd=1, width=70, show='*')  # Increased font size and widened input box
#         entry3.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

#         # Checkbox to show or hide password
#         check_button = Checkbutton(frame, text="Show Password", variable=check_var, onvalue=True, offvalue=False, command=toggle_password, font="arial 16", bg='darkgray', fg="white")  # Updated colors
#         check_button.grid(row=4, column=1, pady=5, sticky='w')

#         # Button to protect the PDF file
#         Protect_button = Button(root, text="Protect PDF File", compound=LEFT, width=20, height=1, bg="#bfb9b9", font="arial 16 bold", command=Protect)  # Increased font size
#         Protect_button.pack(side=BOTTOM, pady=25)

#     # Call the layout adjustment function
#     adjust_layout()

#     # Set the main window's background color
#     root.configure(bg='darkgray')  # Set the background color of the root window

#     # Start the Tkinter mainloop
#     root.mainloop()

# if __name__ == "__main__":
#     create_pdf_locker()



import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader

def create_pdf_locker():
    # Create the main window
    root = Tk()
    root.title("Pdf Protector")

    # Set fullscreen mode
    fullscreen = True
    root.attributes("-fullscreen", fullscreen)

    # Absolute path to the icon and top banner image
    icon_path = r"Pdf_Locker\images\application_top_icon.png"
    banner_path = r"Pdf_Locker\images\top_banner.png"

    # Check if the image exists and set it as the icon
    if os.path.exists(icon_path):
        image_icon = PhotoImage(file=icon_path)
        root.iconphoto(False, image_icon)
    else:
        print(f"Icon image not found: {icon_path}")

    # Variables for the form
    source = StringVar()
    target = StringVar()
    password = StringVar()
    check_var = BooleanVar()  # Define check_var for toggling password visibility

    # Function to browse the source PDF file
    def browse_source():
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select Source PDF File",
                                              filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
        if filename:  # Check if a file was selected
            source.set(filename)  # Set the selected file path to the source variable

    # Function to browse the target PDF file
    def browse_target():
        target_filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                                       title="Select Target PDF File",
                                                       defaultextension=".pdf",
                                                       filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
        if target_filename:  # Check if a file was selected
            target.set(target_filename)  # Set the selected file path to the target variable

    # Function to protect the PDF with a password
    def Protect():
        mainfile = source.get()
        protectfile = target.get()
        code = password.get()

        if mainfile == "" or protectfile == "" or code == "":
            messagebox.showerror("Invalid", "All fields are required!")
            return

        try:
            out = PdfWriter()
            file = PdfReader(mainfile)
            num = len(file.pages)

            for idx in range(num):
                page = file.pages[idx]
                out.add_page(page)

            # Password
            out.encrypt(code)

            with open(protectfile, "wb") as f:
                out.write(f)

            messagebox.showinfo("Success", "PDF protected successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Toggle to show or hide password
    def toggle_password():
        entry3.config(show='' if check_var.get() else '*')

    # Function to exit the application
    def exit_application():
        root.destroy()  # Close the application

    # Override the close button behavior
    root.protocol("WM_DELETE_WINDOW", exit_application)

    # Bind F11 for fullscreen toggle and Esc for exit
    root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
    root.bind("<Escape>", exit_application)

    # Load and display the top banner image if it exists
    if os.path.exists(banner_path):
        Top_image = PhotoImage(file=banner_path)
        Label(root, image=Top_image).pack(fill=X)
    else:
        print(f"Top banner image not found: {banner_path}")

    # Frame for the form
    frame = Frame(root, bd=5, relief=GROOVE, bg='darkgray')  # Set the frame background color
    frame.place(relx=0.01, rely=0.35, relwidth=0.98, relheight=0.6)

    # Adjust the layout of the form
    def adjust_layout():
        global entry1, entry2, entry3  # Declare these as global so they can be used throughout the code

        # Clear previous layout
        for widget in frame.winfo_children():
            widget.grid_forget()

        # Configure grid columns to expand
        frame.grid_columnconfigure(0, weight=1)  # Label column
        frame.grid_columnconfigure(1, weight=5)  # Entry column

        # Source PDF File Location Section
        Label(frame, text="Source PDF File Location:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=0, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
        entry1 = Entry(frame, textvariable=source, font="arial 16", bd=1, width=70)  # Increased font size and widened input box
        entry1.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        Button(frame, text="Select PDF", width=12, bg="#d3cdcd", command=browse_source).grid(row=1, column=1, padx=10, pady=(5, 15), sticky='e')

        # Target PDF File Name Section
        Label(frame, text="Target PDF File Name:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=2, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
        entry2 = Entry(frame, textvariable=target, font="arial 16", bd=1, width=70)  # Increased font size and widened input box
        entry2.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        # Write User Password Section
        Label(frame, text="Write User Password:", font="arial 18 bold", fg="white", bg='darkgray', anchor='w').grid(row=3, column=0, padx=(0, 10), pady=5, sticky='e')  # Updated text color and background
        entry3 = Entry(frame, textvariable=password, font="arial 16", bd=1, width=70, show='*')  # Increased font size and widened input box
        entry3.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        # Checkbox to show or hide password
        check_button = Checkbutton(frame, text="Show Password", variable=check_var, onvalue=True, offvalue=False, command=toggle_password, font="arial 16", bg='darkgray', fg="white")  # Updated colors
        check_button.grid(row=4, column=1, pady=5, sticky='w')

        # Button to protect the PDF file
        Protect_button = Button(root, text="Protect PDF File", compound=LEFT, width=20, height=1, bg="#bfb9b9", font="arial 16 bold", command=Protect)  # Increased font size
        Protect_button.pack(side=BOTTOM, pady=25)

    # Call the layout adjustment function
    adjust_layout()

    # Set the main window's background color
    root.configure(bg='darkgray')  # Set the background color of the root window

    # Start the Tkinter mainloop
    root.mainloop()

if __name__ == "__main__":
    create_pdf_locker()

