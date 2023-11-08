import os
import shutil

# The directory where the files will be taken
source_directory = "insert the path to the directory - i recommend using the download folder"


# Here is the dictionary that will redirect the files according to their type in the corresponding folder
# To add a new type of file, you must add a key -> ex: "doc" and a value -> ex: path of the document

# Directorul destinație pentru fiecare categorie
destination_directory = {
    "pdf": "insert path to the folder",
    "png": "insert path to the folder",
    "jpg": "insert path to the folder",
    "doc": "insert path to the folder",
    "docx": "insert path to the folder",
    "zip": "insert path to the folder"
}

# Checks if the destination directories exist and, if not, creates them
for director in destination_directory.values():
    os.makedirs(director, exist_ok=True)

# Loop through the files in the source directory
for file_name in os.listdir(source_directory):
    full_path = os.path.join(source_directory, file_name)

    # Get the file extension
    if os.path.isfile(full_path):
        extension = file_name.split(".")[-1].lower()

        # Move the file to the appropriate directory
        if extension in destination_directory:
            current_directory = destination_directory[extension]
            shutil.move(full_path, os.path.join(current_directory, file_name))
            print(f"Fisierul {file_name} a fost mutat in {current_directory}")

