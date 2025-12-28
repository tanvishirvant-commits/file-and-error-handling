#Task 1
file_handler=open("sample.txt",'rt')
print(file_handler)
content=file_handler.read()
print(content)
with open("sample.txt",'r') as file:
    line_num=1
    for line in file:
        print(f"Line{line_num}:{line.strip()}")
        line_num +=1
#Task 2
Text=input("Enter text to write to the file:")
with open('output.txt','w') as file:
    file.write(Text + '\n')
    print("Data successfully written to output.txt")

second_text=input("Enter additional text to append:")
with open('output.txt','a') as file:
    file.write(second_text + '\n')
    print("Data successfully append to: output.txt")

print("Final content of output.txt:")
with open('output.txt','r') as file:
    content=file.read()
    print(content)
