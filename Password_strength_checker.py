import customtkinter as ctk
import re

# Function to check password strength
def check_password_strength():
    password = entry.get()
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("• At least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("• Add uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("• Add lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("• Add number")

    if re.search(r"[!@#$%^&*(),.?\"/:{}|<>]", password):
        strength += 1
    else:
        remarks.append("• Add special character")

    if strength == 5:
        result.configure(text="✅ Strong Password!", text_color="#00ff0d")
    elif 3 <= strength < 5:
        result.configure(
            text="⚠️ Moderate Password:\n" + "\n".join(remarks),
            text_color="orange"
        )
    else:
        result.configure(
            text="❌ Weak Password:\n" + "\n".join(remarks),
            text_color="red"
        )

# Create main window
ctk.set_appearance_mode("System")  # Options: "System" | "Light" | "Dark"
ctk.set_default_color_theme("D:/Python materials/python practice/cc/nordic_theme.json")

root = ctk.CTk()
root.title("Password Strength Checker")
root.geometry("600x400")

# Widgets
title = ctk.CTkLabel(root, text="🔒 Password Strength Checker", font=("Bitcount Grid Single Light Open", 30,"bold"))
title.pack(pady=20)

entry = ctk.CTkEntry(root, placeholder_text="Enter your password",font=("Consolas",16), width=300, show="*")
entry.pack(pady=20)

button = ctk.CTkButton(root, text="Check Strength",font=("courier new", 16,"bold"), command=check_password_strength)
button.pack(pady=20)

result = ctk.CTkLabel(root, text="", font=("courier new", 16,"bold"))
result.pack(pady=10)

root.mainloop()

# Written by; Gowsik Raja.S 
# Copyright ©SGR-2006