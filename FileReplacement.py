import os

def get_files_in_folder(folder_path):
    file_names = []
    for entry in os.scandir(folder_path):
        if entry.is_file():
            file_names.append(entry.name)
    return len(file_names), file_names

def copy_and_rename_file(source_file_path, target_file_path):
    with open(source_file_path, "rb") as sf, open(target_file_path, "wb") as tf:
        tf.write(sf.read())

def replace_all_files_in_folder(folder1_path, folder2_path, single_file_path):
    num_files, file_names = get_files_in_folder(folder1_path)
    for file_name in file_names:
        # prefix, suffix = os.path.splitext(file_name) # no longer needed
        new_full_path = os.path.join(folder2_path, file_name) # use original file name instead of single file name
        copy_and_rename_file(single_file_path, new_full_path)

folder1 = input("Enter the first folder path: ")
folder2 = input("Enter the second folder path: ")
single_file = input("Enter the single file path: ")

replace_all_files_in_folder(folder1, folder2, single_file)
