import re
import tkinter as tk

# Function to check password strength
def check_password_strength():
    password = password_entry.get()
    strength = 0
    
    # Criteria checks
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Update slider and label based on strength
    strength_slider.set(strength)
    update_slider_color(strength)

    # Update feedback text
    if strength == 5:
        result_label.config(text="Strong password!")
    elif 3 <= strength < 5:
        result_label.config(text="Moderate password. Consider adding more variety.")
    else:
        result_label.config(text="Weak password. Try adding uppercase letters, digits, and special characters.")

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

# Set up the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x220")

# Password entry field
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

# Slider to show strength score
strength_slider = tk.Scale(root, from_=1, to=5, orient="horizontal", length=200, state="active")
strength_slider.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Start the GUI loop
root.mainloop()
