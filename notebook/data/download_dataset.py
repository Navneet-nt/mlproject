import kagglehub
import shutil
import os

# Download the dataset
default_path = kagglehub.dataset_download("bhavikjikadara/student-study-performance")

# Define your desired download location
custom_path = r"C:\ML Projects\mlproject\notebook\data"

# Move all files from default_path to custom_path
if os.path.exists(default_path):
    for file_name in os.listdir(default_path):
        shutil.move(os.path.join(default_path, file_name), custom_path)
    print(f"Files moved to {custom_path}")
else:
    print("Download path does not exist.")
