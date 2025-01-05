import os
import random
import shutil
import argparse

def get_next_folder_name(base_folder, n):
    """Generate the folder name in the format hdr_data(n)."""
    return os.path.join(base_folder, f"hdr_data{n}")

def select_random_files(source_folder, destination_folder, num_folders, num_files_per_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Get a list of files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Check if there are enough files
    total_files_needed = num_folders * num_files_per_folder
    if len(files) < total_files_needed:
        print(f"Not enough files in the source folder. Found {len(files)} files, need {total_files_needed}.")
        return

    # Randomly select files
    selected_files = random.sample(files, total_files_needed)

    # Distribute files into output folders
    for i in range(num_folders):
        folder_name = get_next_folder_name(destination_folder, i + 1)
        os.makedirs(folder_name, exist_ok=True)

        # Select files for this folder
        start_index = i * num_files_per_folder
        end_index = start_index + num_files_per_folder
        files_to_copy = selected_files[start_index:end_index]

        # Copy selected files to the new folder
        for file_name in files_to_copy:
            source_file_path = os.path.join(source_folder, file_name)
            destination_file_path = os.path.join(folder_name, file_name)
            shutil.copy2(source_file_path, destination_file_path)

        print(f"Copied {num_files_per_folder} files to '{folder_name}'.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Select random files from a folder and copy them to multiple new folders.')
    parser.add_argument('source_folder', help='Path to the source folder')
    parser.add_argument('base_destination_folder', help='Base path for the destination folders')
    parser.add_argument('num_folders', type=int, help='Number of output folders to create')
    parser.add_argument('num_files_per_folder', type=int, help='Number of files to copy to each folder')

    args = parser.parse_args()

    # Run the function with the provided arguments
    select_random_files(args.source_folder, args.base_destination_folder, args.num_folders, args.num_files_per_folder)
