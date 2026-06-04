import os
import shutil

print("===================================")
print("     TASK AUTOMATION PROJECT")
print("===================================\n")

# Folder paths
source_folder = "./source_folder"
destination_folder = "./destination_folder"

# Check source folder exists
if not os.path.exists(source_folder):
    print("❌ Source folder not found!")
    exit()

# Create destination folder if not exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Counter
moved_files = 0

# Loop through files
for file in os.listdir(source_folder):

    # Check JPG files
    if file.endswith(".jpg"):

        # Create full paths
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Move file
        shutil.move(source_path, destination_path)

        print(f"✅ Moved: {file}")

        moved_files += 1

# Final Result
print("\n===================================")

if moved_files == 0:
    print("⚠ No JPG files found.")
else:
    print(f"🎉 Successfully moved {moved_files} JPG files!")

print("===================================")