print("")
input_file=input("Enetr a file to count its words:")

try:
    data = open(input_file)
except:
    print("No such file found!!")
    quit()

line = data.read()

words = line.split()

count = dict()

for i in words:
    count[i]=count.get(i,0)+1

sum=0

for i in count:
    sum=sum+count[i]

print("")
print("Total Number of words:",sum)