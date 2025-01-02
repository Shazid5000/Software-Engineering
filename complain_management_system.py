import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import os
import json

class Complaint:
    def __init__(self, name, address, complaint_text):
        self.name = name
        self.address = address
        self.complaint_text = complaint_text

    def display(self):
        return f"Name: {self.name}\nAddress: {self.address}\nComplaint: {self.complaint_text}\n"

    def to_dict(self):
        return {"name": self.name, "address": self.address, "complaint_text": self.complaint_text}

class ComplaintManagementSystem:
    def __init__(self, filepath="complaints.json"):
        self.complaints = []
        self.filepath = filepath
        self.load_complaints()

    def add_complaint(self, name, address, complaint_text):
        complaint = Complaint(name, address, complaint_text)
        self.complaints.append(complaint)
        self.save_complaints()

    def delete_complaint(self, index):
        if 0 <= index < len(self.complaints):
            del self.complaints[index]
            self.save_complaints()
            return True
        return False

    def get_complaints(self):
        if not self.complaints:
            return "No complaints found."
        complaint_list = "Complaint List:\n\n"
        for idx, complaint in enumerate(self.complaints, 1):
            complaint_list += f"{idx}. {complaint.display()}\n"
        return complaint_list

    def save_complaints(self):
        with open(self.filepath, "w") as f:
            json.dump([c.to_dict() for c in self.complaints], f)

    def load_complaints(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                data = json.load(f)
                for item in data:
                    self.complaints.append(Complaint(**item))

# Tkinter GUI
class ComplaintApp:
    def __init__(self, root, cms):
        self.root = root
        self.cms = cms
        self.root.title("Complaint Management System")
        
        # Set fullscreen
        self.root.state("zoomed")
        
        # Set background color
        self.root.configure(bg="#2F2F2F")  # Dark gray

        # Center frame with padding for larger size and dark background
        frame = tk.Frame(root, bg="#2F2F2F")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Labels and entries with larger font, spacing, and new color scheme
        tk.Label(frame, text="Name:", anchor="center", font=("Arial", 24), fg="white", bg="#2F2F2F").grid(row=0, column=0, padx=20, pady=20, sticky="e")
        self.name_entry = tk.Entry(frame, font=("Arial", 22), justify="center", width=20, bg="#000000", fg="white")
        self.name_entry.grid(row=0, column=1, padx=20, pady=20)
        self.name_entry.bind("<FocusIn>", self.check_empty)

        tk.Label(frame, text="Address:", anchor="center", font=("Arial", 24), fg="white", bg="#2F2F2F").grid(row=1, column=0, padx=20, pady=20, sticky="e")
        self.address_entry = tk.Entry(frame, font=("Arial", 22), justify="center", width=20, bg="#000000", fg="white")
        self.address_entry.grid(row=1, column=1, padx=20, pady=20)
        self.address_entry.bind("<FocusIn>", self.check_empty)

        tk.Label(frame, text="Complaint:", anchor="center", font=("Arial", 24), fg="white", bg="#2F2F2F").grid(row=2, column=0, padx=20, pady=20, sticky="ne")
        self.complaint_text = tk.Text(frame, width=40, height=8, font=("Arial", 22), wrap="word", bg="#000000", fg="white")
        self.complaint_text.grid(row=2, column=1, padx=20, pady=20)
        self.complaint_text.bind("<FocusIn>", self.check_empty)

        # Buttons with larger font and dark background
        self.add_button = tk.Button(frame, text="Add Complaint", font=("Arial", 20), command=self.add_complaint, width=20, height=2, bg="#000000", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.view_button = tk.Button(frame, text="View Complaints", font=("Arial", 20), command=self.view_complaints, width=20, height=2, bg="#000000", fg="white")
        self.view_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(frame, text="Delete Complaint", font=("Arial", 20), command=self.ask_for_password, width=20, height=2, bg="#000000", fg="white")
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

    def check_empty(self, event):
        widget = event.widget
        if not widget.get() and isinstance(widget, (tk.Entry, tk.Text)):
            widget.config(fg="white")

    def add_complaint(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        complaint_text = self.complaint_text.get("1.0", tk.END).strip()
        if not name or not address or not complaint_text:
            messagebox.showerror("Error", "All fields are required!")
            return
        self.cms.add_complaint(name, address, complaint_text)
        messagebox.showinfo("Success", "Complaint added successfully!")
        self.clear_entries()

    def view_complaints(self):
        complaints = self.cms.get_complaints()
        messagebox.showinfo("Complaints", complaints)

    def ask_for_password(self):
        # Prompt the user to enter the password
        password = simpledialog.askstring("Password", "Enter password to delete complaints:", show="*")
        if password == "11":
            self.open_delete_complaint_window()
        else:
            messagebox.showerror("Error", "Incorrect password. Access denied.")

    def open_delete_complaint_window(self):
        # Create a new Toplevel window for complaint number input
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Complaint")
        delete_window.geometry("400x200")
        delete_window.configure(bg="#2F2F2F")

        tk.Label(delete_window, text="Enter Complaint Number to Delete:", font=("Arial", 18), fg="white", bg="#2F2F2F").pack(pady=20)

        # Complaint number entry
        complaint_number_entry = tk.Entry(delete_window, font=("Arial", 22), width=10, bg="#000000", fg="white")
        complaint_number_entry.pack(pady=10)

        def delete_complaint_action():
            try:
                index = int(complaint_number_entry.get()) - 1  # Convert to zero-based index
                if self.cms.delete_complaint(index):
                    messagebox.showinfo("Success", f"Complaint {index + 1} deleted successfully.")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error", "Invalid complaint number.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid complaint number.")

        # Delete button
        delete_button = tk.Button(delete_window, text="Delete", font=("Arial", 18), command=delete_complaint_action, bg="#000000", fg="white")
        delete_button.pack(pady=10)

        # Close button
        close_button = tk.Button(delete_window, text="Close", font=("Arial", 18), command=delete_window.destroy, bg="#000000", fg="white")
        close_button.pack(pady=10)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.complaint_text.delete("1.0", tk.END)

# Main program
cms = ComplaintManagementSystem()
root = tk.Tk()
app = ComplaintApp(root, cms)
root.mainloop()
