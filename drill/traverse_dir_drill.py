import os

dir_path = os.path.join("parent_dir", "sub_dir")
for home, dirs, files in os.walk(dir_path):
    print(home)
    print(dirs)
    print(files)
    files_list = []
    for i in dirs:
        files_list.append(os.listdir(os.path.join(dir_path, i)))
