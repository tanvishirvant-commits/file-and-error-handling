#Task 1
file_handler=open("sample txt")
print(file_handler)
content=file_handler.read()
print(content)


import os
file_name="sample.txt"
if os.path.exists(file_name):
    print("The file sample.txt found")
else:
    print(f"Error:The file {'sample.txt'} was not found")

#Task 2
fh=open("output.txt",'wt')
Text=input("Enter text to write to the file:")
fh=open("output.txt",'at')
fh.write("Learning file handling in python")
fh.close()


