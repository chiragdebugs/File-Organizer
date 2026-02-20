import os
import shutil

print("=== Professional File Organizer ===")

folder_path = input("Enter folder path to organize (example: ~/Downloads or ~/Desktop): ")
folder_path = os.path.expanduser(folder_path)

if not os.path.exists(folder_path):
    print("Error: Folder does not exist.")
    exit()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Programs": [".dmg", ".pkg", ".exe"],
    "Python": [".py"],
    "Others": []
}

for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

moved_count = 0

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                moved_count += 1
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))
            print(f"Moved: {file} → Others")
            moved_count += 1

print(f"\nDone. Total files organized: {moved_count}")