import os
import shutil
import glob
def manage_os():
    source_folder = os.getcwd()
    destination_folder = input("Enter your path path/where/you/want/backup : ") 
    if not os.path.exists(destination_folder):
        print("wrong path, please enter it carfully!")
        return manage_os()
    destination_folder += "\\backup"
    os.makedirs(destination_folder , exist_ok=True)
    noCopies = 0
    for file_path in glob.glob(os.path.join(source_folder, "*.txt")):
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(destination_folder, file_name)
        shutil.copy(file_path, dest_path)
        print(f"Copied: {file_name}")
        noCopies += 1
    
    print("All .txt files ({noCopies} files) copied successfully!")
