import os
import shutil

# Path to the folder containing your screenshots
SOURCE_FOLDER = "C:/Users/YourName/Pictures/GameScreenshots"  # <- change this
DEST_FOLDER = os.path.join(SOURCE_FOLDER, "Organized")

# Create destination folder if it doesn't exist
os.makedirs(DEST_FOLDER, exist_ok=True)

# File extensions to organize
IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg"]

# Counter for renamed files
counter = 1

for filename in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, filename)
    if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in IMAGE_EXTENSIONS:
        new_name = f"screenshot_{counter}{os.path.splitext(filename)[1].lower()}"
        new_path = os.path.join(DEST_FOLDER, new_name)
        shutil.move(file_path, new_path)
        counter += 1

print(f"Organized {counter - 1} screenshots into '{DEST_FOLDER}'.")
