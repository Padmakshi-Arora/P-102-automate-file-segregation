import os
import shutil

from_dir = "C:/Users/HP/Downloads"
to_dir = "C:/Users/HP/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

#Move all image files from downloads folder to another folder
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+"Document_Files"
        path3 = to_dir+"Document_Files"+'/'+file_name

#check if folder/directory path exists before moving
#else make a new folder/directory then move

if os.path.exists(path2):
    print("Moving " + file_name + ".....")

    #move from path1 ---> path3
    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Moving " + file_name + ".....")
    shutil.move(path1, path3)