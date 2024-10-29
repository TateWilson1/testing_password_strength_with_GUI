import re
import tkinter as tk

# Function to check password strength
def check_password_strength(event=None):
    password = password_entry.get()
    strength = 0
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    
    # Count the number of criteria met
    strength += length_criteria
    strength += uppercase_criteria
    strength += lowercase_criteria
    strength += digit_criteria
    strength += special_char_criteria
    
    # Update slider and label based on strength
    strength_slider.set(strength)
    update_slider_color(strength)

    # Update feedback text
    if strength == 5:
        result_label.config(text="Strong password!")
    elif 3 <= strength < 5:
        result_label.config(text="Moderate password. Consider adding more variety.")
    else:
        missing_criteria = []
        if not length_criteria:
            missing_criteria.append("8 characters")
        if not uppercase_criteria:
            missing_criteria.append("uppercase letters")
        if not lowercase_criteria:
            missing_criteria.append("lowercase letters")
        if not digit_criteria:
            missing_criteria.append("digits")
        if not special_char_criteria:
            missing_criteria.append("special characters")
        result_label.config(text="Weak password. Consider adding: " + ", ".join(missing_criteria))

# Function to update slider color based on strength
def update_slider_color(strength):
    # Define color mapping based on strength
    colors = {
        1: "red",
        2: "orange",
        3: "yellow",
        4: "lightgreen",
        5: "green"
    }
    color = colors.get(strength, "red")
    strength_slider.config(troughcolor=color)  # Change slider background color

# Function to clear input and results
def clear_input():
    password_entry.delete(0, tk.END)
    strength_slider.set(0)
    result_label.config(text="")

# Function to toggle password visibility
def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_button.config(text='Hide Password')
    else:
        password_entry.config(show='*')
        toggle_button.config(text='Show Password')

# Set up the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x300")

# Password entry field
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", check_password_strength)  # Update strength on key release

# Button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

# Button to clear input
clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack(pady=5)

# Toggle password visibility button
toggle_button = tk.Button(root, text="Show Password", command=toggle_password)
toggle_button.pack(pady=5)

# Slider to show strength score
strength_slider = tk.Scale(root, from_=1, to=5, orient="horizontal", length=200, state="active")
strength_slider.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Start the GUI loop
root.mainloop()
