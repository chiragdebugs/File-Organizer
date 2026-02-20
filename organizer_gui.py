import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Programs": [".dmg", ".pkg"],
    "Python": [".py"],
    "Others": []
}

def organize_folder():
    folder_path = filedialog.askdirectory()
    
    if not folder_path:
        return
    
    moved_count = 0

    for folder in file_types:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False

            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    moved = True
                    moved_count += 1
                    break

            if not moved:
                shutil.move(file_path, os.path.join(folder_path, "Others", file))
                moved_count += 1

    messagebox.showinfo("Success", f"Organized {moved_count} files!")

# Create window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

label = tk.Label(root, text="Professional File Organizer", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Select Folder and Organize", command=organize_folder, font=("Arial", 12))
button.pack(pady=20)

root.mainloop()