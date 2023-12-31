file_name = input("Enter file name: ")

try:
    file = open(file_name)
except:
    print(f"Failed to open the file : {file_name}")
    exit()
c=0
for i in file:
    c=c+1
print(f"Number of lines in file :{c}")