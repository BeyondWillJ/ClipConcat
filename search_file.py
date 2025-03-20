import os

def search_files(directory):
    file_l = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_l.append(file)
            print(file)
            print(os.path.join(root, file))
    return file_l.sort()

directory = r".\cls"
if os.path.exists(directory) and os.path.isdir(directory):
    search_files(directory)
else:
    print(f"Directory {directory} does not exist.")