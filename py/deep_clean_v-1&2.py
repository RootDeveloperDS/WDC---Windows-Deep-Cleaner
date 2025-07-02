# -*- coding: utf-8 -*-
'''By Root Developer D.S.'''
import os
import shutil
import subprocess
import webbrowser
import tkinter as tk
from tkinter import messagebox, ttk

def delete_folder_contents(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Error deleting {item_path}: {e}")

def clean_system():
    steps = [
        ("Clearing TEMP folders...", lambda: delete_folder_contents(os.getenv('TEMP'))),
        ("Clearing Windows Temp...", lambda: delete_folder_contents("C:\\Windows\\Temp")),
        ("Clearing Prefetch...", lambda: delete_folder_contents("C:\\Windows\\Prefetch")),
        ("Emptying Recycle Bin...", lambda: subprocess.run("powershell.exe Clear-RecycleBin -Force", shell=True)),
        ("Stopping Windows Update Service...", lambda: subprocess.run("net stop wuauserv", shell=True)),
        ("Cleaning Windows Update Cache...", lambda: delete_folder_contents("C:\\Windows\\SoftwareDistribution\\Download")),
        ("Starting Windows Update Service...", lambda: subprocess.run("net start wuauserv", shell=True)),
        ("Cleaning Chrome Cache...", lambda: delete_folder_contents(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"))),
        ("Cleaning Edge Cache...", lambda: delete_folder_contents(os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache"))),
        ("Cleaning Firefox Cache...", clean_firefox)
    ]

    for i, (desc, func) in enumerate(steps):
        status_label.config(text=desc)
        progress["value"] = (i + 1) * 100 / len(steps)
        app.update_idletasks()
        try:
            func()
        except Exception as e:
            print(f"[Error] {desc}: {e}")

    progress["value"] = 100
    status_label.config(text="Cleaning Complete!")
    messagebox.showinfo("Done", "Deep Clean Completed Successfully!")

def clean_firefox():
    base_path = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
    if os.path.exists(base_path):
        for profile in os.listdir(base_path):
            cache_path = os.path.join(base_path, profile, "cache2")
            delete_folder_contents(cache_path)

def open_Github():
    webbrowser.open("https://github.com/RootDeveloperDS")  # <-- Replace this with your actual site or GitHub

# GUI Setup
app = tk.Tk()
app.title("Root Developer - Windows Deep Cleaner")
app.geometry("420x310")
app.resizable(False, False)

tk.Label(app, text="Deep Cleaner", font=("Helvetica", 18, "bold")).pack(pady=10)
status_label = tk.Label(app, text="Click to Begin Cleaning", font=("Arial", 10))
status_label.pack()

progress = ttk.Progressbar(app, length=350, mode='determinate')
progress.pack(pady=10)

tk.Button(app, text="Start Deep Cleaning", command=clean_system, bg="#dc3545", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# Github + Branding
tk.Button(app, text="Visit our Github", command=open_Github, bg="#007BFF", fg="white", font=("Arial", 10)).pack()
tk.Label(app, text="Built by Root Developer D.S.", font=("Arial", 9), fg="gray").pack(side="bottom", pady=10)

tk.Label(app, text="Version 1.0", font=("Arial", 8), fg="gray").pack(side="bottom")


import sys
from PIL import Image, ImageTk

# Function to get the path to the image whether running as .py or .exe
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Load the logo using the safe path
logo_path = resource_path("root_logo.png")
logo_img = Image.open(logo_path)
logo_img = logo_img.resize((20, 20))
logo_icon = ImageTk.PhotoImage(logo_img)


# Footer Frame for logo + text
footer_frame = tk.Frame(app)
footer_frame.pack(side="bottom", pady=10)

# Logo label
tk.Label(footer_frame, image=logo_icon).pack(side="left", padx=5)

# Text label
tk.Label(footer_frame, text="Built by Root Developer", font=("Arial", 9), fg="gray").pack(side="left")

# Prevent image from being garbage-collected
app.logo_icon = logo_icon


app.mainloop()