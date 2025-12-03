import shutil

shutil.copy("source.txt", "destination.txt")
print("File copied successfully!")


import shutil
shutil.copy2("Source.txt","backup_source.txt")
print("copied wiht metadata")


import shutil 
shutil.copytree("my_folder", "my_folder_breacup")
print("Folder  copied succesufully")


import shutil

shutil.rmtree("old_logs")
print("Folder removed!")

import shutil

shutil.rmtree("old_logs")
print("Folder removed!")

import shutil

shutil.rmtree("old_logs")
print("Folder removed!")

import shutil

shutil.unpack_archive("my_backup.zip", "extracted_folder")
print("Archive extracted!")


import shutil

disk = shutil.disk_usage("/")
print("Total:", disk.total)
print("Used :", disk.used)
print("Free :", disk.free)