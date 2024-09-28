import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Initial data
users = {
    "admin": {"password": "admin123"},  # admin credentials
    "12345": {"name": "John Doe", "password": "pass123"},  # student credentials
    "67890": {"name": "Jane Smith", "password": "pass456"}
}
complaints = []

# Main application class
class ComplaintManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Complaint Management System")
        self.geometry("800x600")
        self.username = None  # Track the logged-in username

        # Initial frame
        self.current_frame = None
        self.switch_frame(MainLoginFrame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

class MainLoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Load the background image
        self.bg_image = Image.open(r"C:\Users\Rohit\Documents\Project\Python projects\Complaint Management System Mini Project\htc.jpg")
        self.bg_image = self.bg_image.resize((800, 600), Image.BILINEAR)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a canvas
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        
        # Set the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Add login option buttons# Get the bounding box of the text    
        x, y = 400, 100  # Coordinates where the text is placed
        text_width1 = 430  # Adjust this value according to the width of the text
        text_height1 = 50  # Adjust this value according to the height of the text

        # Calculate the coordinates for the background rectangle
        x1 = x - text_width1/2
        y1 = y - text_height1/2
        x2 = x + text_width1/2
        y2 = y + text_height1/2

        # Create a rectangle as the background for the text
        bg_rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="brown")

        # Create the text on top of the background rectangle
        text1 = self.canvas.create_text(x, y, text="Complaint Management System", font=("Arial", 22), fill="White")

        # Ensure that the text is displayed on top of the background rectangle
        self.canvas.tag_raise(text1)

        # Add login option buttons# Get the bounding box of the text    
        x, y = 380, 200  # Coordinates where the text is placed
        text_width = 240  # Adjust this value according to the width of the text
        text_height = 40  # Adjust this value according to the height of the text

        # Calculate the coordinates for the background rectangle
        x1 = x - text_width/2
        y1 = y - text_height/2
        x2 = x + text_width/2
        y2 = y + text_height/2

        # Create a rectangle as the background for the text
        bg_rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

        # Create the text on top of the background rectangle
        text = self.canvas.create_text(x, y, text="Choose Login Type", font=("Arial", 16), fill="black")

        # Ensure that the text is displayed on top of the background rectangle
        self.canvas.tag_raise(text)

        self.admin_button = tk.Button(self, text="Admin Login", width=13, height=1, font=("Arial", 12), command=lambda: master.switch_frame(AdminLoginFrame))
        self.student_button = tk.Button(self, text="Student Login", width=13, height=1, font=("Arial", 12), command=lambda: master.switch_frame(StudentLoginFrame))
        
        self.canvas.create_window(380, 280, window=self.admin_button)
        self.canvas.create_window(380, 330, window=self.student_button)

class AdminLoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Admin Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack()
        tk.Button(self, text="Back", command=lambda: master.switch_frame(MainLoginFrame)).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and username in users and users[username]["password"] == password:
            self.master.username = username
            self.master.switch_frame(AdminFrame)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

class StudentLoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Roll Number:").pack()
        self.roll_number_entry = tk.Entry(self)
        self.roll_number_entry.pack()

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack()
        tk.Button(self, text="Back", command=lambda: master.switch_frame(MainLoginFrame)).pack()

    def login(self):
        roll_number = self.roll_number_entry.get()
        password = self.password_entry.get()
        
        if roll_number in users and users[roll_number]["password"] == password:
            self.master.student = {"roll_number": roll_number, "name": users[roll_number]["name"]}
            self.master.switch_frame(UserFrame)
        else:
            messagebox.showerror("Login Failed", "Invalid roll number or password.")

class UserFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        student_name = self.master.student["name"]

        tk.Label(self, text=f"Welcome, {student_name}!").pack()

        tk.Button(self, text="Register Complaint", command=lambda: master.switch_frame(RegisterComplaintFrame)).pack()
        tk.Button(self, text="Logout", command=lambda: master.switch_frame(MainLoginFrame)).pack()

class RegisterComplaintFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        tk.Label(self, text="Enter your complaint:").pack()
        self.complaint_entry = tk.Entry(self)
        self.complaint_entry.pack()

        tk.Button(self, text="Submit", command=self.register_complaint).pack()
        tk.Button(self, text="Back", command=lambda: master.switch_frame(UserFrame)).pack()

    def register_complaint(self):
        complaint = self.complaint_entry.get()
        if complaint:
            student_info = self.master.student
            complaints.append({"roll_number": student_info["roll_number"], "name": student_info["name"], "complaint": complaint})
            messagebox.showinfo("Success", "Complaint registered successfully!")
            self.master.switch_frame(UserFrame)
        else:
            messagebox.showerror("Error", "Complaint cannot be empty.")

class AdminFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Admin Panel").pack()
        tk.Button(self, text="View Complaints", command=self.view_complaints).pack()
        tk.Button(self, text="Logout", command=lambda: master.switch_frame(MainLoginFrame)).pack()
    
    def view_complaints(self):
        if complaints:
            complaints_str = "\n".join([f"{i+1}. {c['roll_number']} - {c['name']}: {c['complaint']}" for i, c in enumerate(complaints)])
            messagebox.showinfo("Complaints", complaints_str)
        else:
            messagebox.showinfo("Complaints", "No complaints registered yet.")

if __name__ == "__main__":
    app = ComplaintManagementSystem()
    app.mainloop()
