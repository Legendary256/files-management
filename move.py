import os
import random
import shutil
import argparse

class Copy:
    def __init__(self, args):
        self.path_to_file_paths_file = args.path_to_file_paths_file
        self.destination_folder = args.path_to_destination
        self.file_paths = list()

    def random_string(self, length: int) -> str:
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "".join(random.choice(letters) for i in range(length))

    def open_start(self):
        try:
            with open(self.path_to_file_paths_file, "r") as file:
                self.file_paths = file.readlines()
        except FileNotFoundError:
            print(f"Error: file {self.file_to_file_paths_file} not found")
            exit(1)

    def open_dest(self):
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

    def copy_files(self):
        for i, file_path in enumerate(self.file_paths):
            file_path = file_path.strip()
            try:
                filename, ext = os.path.splitext(os.path.basename(file_path))
                new_filename = self.random_string(50) + ext
                new_file_path = os.path.join(self.destination_folder, new_filename)
                shutil.copy2(file_path, new_file_path)
                print(f"Copied file {i+1} to {new_file_path}")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error: {e}")

    def run(self):
        self.open_start()
        self.open_dest()
        self.copy_files()

def take_args():
    parser = argparse.ArgumentParser(description='Copy file from one folder to another with a random name.')
    parser.add_argument('-file-paths-file', dest='path_to_file_paths_file', required=True, help='Path to file with paths of files that you want to copy.')
    parser.add_argument('-destination-path', dest='path_to_destination', required=True, help='Path to destination folder.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = take_args()
    c = Copy(args).run()