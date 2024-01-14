import os
import random
import shutil
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python create_train_test_valid.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    
    # Input folder containing all the files
    input_folder = sys.argv[1]
    
    # Destination folders for train, test, and valid sets
    train_folder = os.path.join(sys.argv[2],'train/')
    test_folder = os.path.join(sys.argv[2],'test/')
    valid_folder = os.path.join(sys.argv[2],'valid/')
    
    # Create destination folders if they don't exist
    for folder in [train_folder, test_folder, valid_folder]:
        os.makedirs(folder, exist_ok=True)
    
    # Get a list of all files in the input folder
    all_files = os.listdir(input_folder)
    
    # Shuffle the list of files randomly
    random.shuffle(all_files)
    
    # Calculate the number of files for each set
    total_files = len(all_files)
    train_split = int(total_files * 0.85)
    test_split = int(total_files * 0.075)
    valid_split = int(total_files * 0.075)
    
    # Distribute files into train, test, and valid sets
    train_files = all_files[:train_split]
    test_files = all_files[train_split:train_split + test_split]
    valid_files = all_files[train_split + test_split:]
    
    # Move files to their respective destination folders
    for file in train_files:
        source_path = os.path.join(input_folder, file)
        destination_path = os.path.join(train_folder, file)
        shutil.move(source_path, destination_path)
    
    for file in test_files:
        source_path = os.path.join(input_folder, file)
        destination_path = os.path.join(test_folder, file)
        shutil.move(source_path, destination_path)
    
    for file in valid_files:
        source_path = os.path.join(input_folder, file)
        destination_path = os.path.join(valid_folder, file)
        shutil.move(source_path, destination_path)
    
    print(f'Split {total_files} files into train: {train_split}, test: {test_split}, valid: {valid_split}.')

