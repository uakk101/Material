file_path = '/Users/Usman/OneDrive/Desktop/file_system/newfile.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())