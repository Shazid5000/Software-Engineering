import sqlite3
import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter.messagebox import showinfo, showerror, askyesno

# Database handling class
class DBConnect:
    def __init__(self):
        self.conn = sqlite3.connect('complaints.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                gender TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def Add(self, name, gender, description):
        try:
            self.cursor.execute('''
                INSERT INTO complaints (name, gender, description)
                VALUES (?, ?, ?)
            ''', (name, gender, description))
            self.conn.commit()
            return "Complaint added successfully."
        except Exception as e:
            return f"Error adding complaint: {e}"

    def fetch_complaints(self):
        try:
            self.cursor.execute("SELECT id, name, gender, description FROM complaints")
            rows = self.cursor.fetchall()
            return [{"id": row[0], "name": row[1], "gender": row[2], "description": row[3]} for row in rows]
        except Exception as e:
            print(f"Error fetching complaints: {e}")
            return []

    def delete_complaint(self, complaint_id):
        try:
            self.cursor.execute("DELETE FROM complaints WHERE id=?", (complaint_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting complaint: {e}")
            return False

    def close(self):
        self.conn.close()

# Complaint List Class
class ListComp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Complaint List")
        self.geometry("1920x1080")
        self.configure(background='#AEB6BF')

        # Setup Treeview to display complaints
        self.tree = ttk.Treeview(self, columns=("Name", "Gender", "Complaint"), show="headings")
        self.tree.heading("Name", text="Full Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Complaint", text="Complaint")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Delete Button
        delete_button = tk.Button(self, text="Delete Selected", command=self.delete_complaint)
        delete_button.pack(pady=10)

        # Load complaints when window opens
        self.load_complaints()

    def load_complaints(self):
        db = DBConnect()
        complaints = db.fetch_complaints()

        # Clear any existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert fetched complaints into the Treeview with IDs as the iid
        for complaint in complaints:
            self.tree.insert("", tk.END, iid=str(complaint['id']), values=(
                complaint.get('name', 'N/A'),
                complaint.get('gender', 'N/A'),
                complaint.get('description', 'N/A')
            ))

    def delete_complaint(self):
        selected_item = self.tree.selection()
        if not selected_item:
            showerror("Error", "No complaint selected to delete.")
            return

        confirm = askyesno("Confirm Delete", "Are you sure you want to delete the selected complaint?")
        if confirm:
            complaint_id = selected_item[0]  # Use the iid of the selected complaint (which is the complaint ID)
            db = DBConnect()
            success = db.delete_complaint(complaint_id)

            if success:
                self.tree.delete(selected_item)  # Remove from Treeview
                showinfo("Success", "Complaint deleted successfully.")
            else:
                showerror("Deletion Error", "Failed to delete complaint.")

# Main Application with Authentication
def authenticate():
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    return password == "1111"

def ShowList():
    if authenticate():
        listrequest = ListComp()
    else:
        showerror("Authentication Error", "Incorrect password")

def SaveData():
    msg = conn.Add(fullname.get(), SpanGender.get(), Complaint.get(1.0, 'end'))
    fullname.delete(0, 'end')
    Complaint.delete(1.0, 'end')
    showinfo(title='Add Info', message=msg)

# Config
conn = DBConnect()
root = tk.Tk()
root.geometry('1920x1080')
root.title('Complaint Management')
root.configure(background='#AEB6BF')

# Define SpanGender as a global StringVar
SpanGender = tk.StringVar()

# Style
style = ttk.Style()
style.theme_use('classic')
for elem in ['TLabel', 'TButton', 'TRadiobutton']:
    style.configure(elem, background='#AEB6BF', font=('Arial', 20))

# Grid configuration
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Grid Widgets
tk.Label(root, text='Full Name:', font=('Arial', 20)).grid(row=0, column=0, padx=20, pady=20, sticky='w')

tk.Label(root, text='Gender:', font=('Arial', 20)).grid(row=1, column=0, padx=20, pady=20, sticky='w')

tk.Label(root, text='Complaint:', font=('Arial', 20)).grid(row=2, column=0, padx=20, pady=20, sticky='w')

tk.Radiobutton(root, text='Male', value='male', variable=SpanGender, font=('Arial', 20)).grid(row=1, column=1, padx=20, pady=20, sticky='w')
tk.Radiobutton(root, text='Female', value='female', variable=SpanGender, font=('Arial', 20)).grid(row=1, column=2, padx=20, pady=20, sticky='w')

BuList = tk.Button(root, text='List Comp.', command=ShowList, font=('Arial', 20))
BuList.grid(row=1, column=3, padx=20, pady=20, sticky='w')

BuSubmit = tk.Button(root, text='Submit Now', command=SaveData, font=('Arial', 20))
BuSubmit.grid(row=2, column=3, padx=20, pady=20, sticky='w')

# Entries
fullname = tk.Entry(root, width=50, font=('Arial', 20))
fullname.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky='ew')

Complaint = tk.Text(root, width=50, height=10, font=('Arial', 20))
Complaint.grid(row=2, column=1, columnspan=2, padx=20, pady=20, sticky='ew')

root.mainloop()
