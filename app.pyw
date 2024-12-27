import random
import customtkinter as ctk
from tkinter import messagebox as mg
from datetime import datetime

# Character sets
uppercase = "AQWSEDZXCFRTGVBHYUJNMKILOP"
lowercase = uppercase.lower()
numbers = "0123456789"
characters = "!`#$%^&*()_+=-|{}[]//<>.\\"

# Combine all characters based on conditions
all = ""
upper, lower, nums, syms = True, True, True, True

if upper:
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += numbers
if syms:
    all += characters

# Initialize application window
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.geometry("500x300")  # Increased height to accommodate the label and buttons
window.resizable(False, False)
window.title("Password Generator")

# Define the modern font (Segoe UI)
font_style = ('Segoe UI', 14)

# Entry for displaying the generated password
print_password = ctk.CTkEntry(window, width=400, height=40, justify="center", font=('Segoe UI', 20), state="readonly")
print_password.pack(pady=15)

# Label for instructions
length_label = ctk.CTkLabel(window, text="Choose the password length:", font=('Segoe UI', 15))
length_label.pack(pady=5)

# Combobox for selecting password length
values = ["4", "6", "8", "10"]
select_length = ctk.CTkComboBox(
    window, values=values, width=100, height=30, font=('Segoe UI', 15), state="readonly", justify="center"
)
select_length.pack(pady=10)

# Generate password function
def generate_password():
    combovalue = select_length.get()
    try:
        # Convert combobox value to integer
        length = int(combovalue)
        PG(length)
    except ValueError:
        mg.showerror("ValueError", "Please select a valid number.")
        return

# Password generator logic
def PG(length):
    password = "".join(random.sample(all, length))
    print_password.configure(state="normal")  # Allow modification
    print_password.delete(0, "end")  # Clear any existing text
    print_password.insert(0, password)  # Insert the generated password
    print_password.configure(state="disabled")  # Disable the entry again

    # Check if the checkbox is checked before saving the password
    if check_btn_var.get() == 1:  # If checked, save password
        save_password(password)

# Save password with timestamp to a .txt file
def save_password(password):
    # Get the current time in a readable format
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write password and timestamp to a text file
    with open("generated_passwords.txt", "a") as file:
        file.write(f"Password: {password} | Generated at: {current_time}\n")

    mg.showinfo("Password Saved", f"Password saved at {current_time}.")

# Function to handle the CheckButton state change
def on_check_change():
    if check_btn_var.get() == 1:  # If the checkbox is checked
        mg.showinfo("Ready to Save", "Passwords will be saved after generation.")

# Button to trigger password generation
generate_btn = ctk.CTkButton(
    window, text="Generate", width=200, height=40, font=('Segoe UI', 15), command=generate_password
)
generate_btn.pack(pady=10)

# CheckButton to save password to a text file when checked
check_btn_var = ctk.IntVar()  # Variable to hold the state of the checkbox
check_btn = ctk.CTkCheckBox(
    window, text="Check to Save Password", variable=check_btn_var, font=('Segoe UI', 15), command=on_check_change
)
check_btn.pack(pady=10)

# Bind the Enter key to generate the password
window.bind('<Return>', lambda event: generate_password())  # Enter key

# Add Hyperlink
def open_hyperlink(event):
    import webbrowser
    webbrowser.open("https://www.example.com")  # Replace with your desired URL

# Hyperlink label
hyperlink_label = ctk.CTkLabel(window, text="Click here to visit ", font=('Segoe UI', 15, 'underline'), text_color="blue",cursor="hand2")
hyperlink_label.pack(pady=9)

# Bind the label to open the URL when clicked
hyperlink_label.bind("<Button-1>", open_hyperlink)

# Run the application
window.mainloop()

