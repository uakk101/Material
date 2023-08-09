import os



print(os.listdir("/Users/Usman/OneDrive/Desktop"))

print(os.getcwd())


files = os.listdir('/Users/Usman/OneDrive/Documents/')
for file in files:
    print(file)


os.rename("newfile.txt", "ali.txt")

os.mkdir("new_folder")
os.makedirs("new_folder/sub_folder/anothefolder")


os.rmdir("folder")
os.removedirs("new_folder/sub_folder/anothefolder") 

# will remove the sub_folder and new_folder itself recursively


os.rename('/path/to/old_name', '/path/to/new_name')

shutil.rmtree('new_folder/sub_folder')


print(os.listdir("/Users/Usman/OneDrive/Desktop"))

# lets create a new folder in the Users folder

