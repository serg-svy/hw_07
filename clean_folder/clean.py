import os
import sys

def clean_folder(folder_path):


def main():
    if len(sys.argv) != 2:
        print("Usage: clean-folder <folder_path>")
        return
    
    folder_path = sys.argv[1]
    clean_folder(folder_path)

if __name__ == "__main__":
    main()
