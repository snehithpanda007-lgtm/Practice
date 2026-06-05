import os
import shutil

# Categories and their file extensions
extensions = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

# Get folder path from user
folder_path = input("Enter folder path: ")

# Store count for summary
summary = {
    "Images": 0,
    "Documents": 0,
    "Videos": 0,
    "Others": 0
}

# Scan all items in folder
for item in os.listdir(folder_path):

    # Create full path
    full_path = os.path.join(folder_path, item)

    # Skip folders, process only files
    if not os.path.isfile(full_path):
        continue

    # Extract extension
    name, extension = os.path.splitext(item)

    # Default category
    category = "Others"

    # Find matching category
    for folder_name, ext_list in extensions.items():
        if extension.lower() in ext_list:
            category = folder_name
            break

    # Create destination folder path
    destination_folder = os.path.join(folder_path, category)

    # Create folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Destination file path
    destination_path = os.path.join(destination_folder, item)

    # Move file
    shutil.move(full_path, destination_path)

    # Update count
    summary[category] += 1

    print(f"Moved: {item} -> {category}")

# Print summary
print("\nSummary")
print("-" * 20)

for category, count in summary.items():
    print(f"{category}: {count}")