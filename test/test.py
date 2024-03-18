#write a code that put all the code files into a folders with a name like the files
#i save a files like number.name.py so the folder will be number.name

import os
import shutil

def main():
    for filename in os.listdir("."):
        if filename.endswith(".py"):
            folder_name = filename.split(".")[0]
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            shutil.move(filename, folder_name)
            print(f"{filename} moved to {folder_name}")
            
if __name__ == "__main__":
    main()
    
