# file_path = '/Users/Usman/OneDrive/Desktop/file_system/newfile.txt'

# # Open the file in write mode
# file = open(file_path, 'w')
# file.close()

# # File creation complete
# print('File created:', file_path)




file_path = '/Users/Usman/OneDrive/Desktop/file_system/newfile.txt'

# Open the file in write mode
with open(file_path, 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a new file created in Python.')

# File creation and writing complete
print('File created:', file_path)