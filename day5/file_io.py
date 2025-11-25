f = open("myfile.txt",'r')
f= open("myfile.txt","w")
f.write("hello, world!")

f = open("myfile.txt","r")
f.close()

with open("myfile.txt","r") as f:

 f= open("myfile.txt", "r")
 f= open ('myfile.txt',"w")
 f.write("this is the one of the my first file to get the ")

 f = open("myfile.txt","r")
 content = f.read()
 print(content)

 with  open("myfile.txt","w") as f:
   content=f.write("ther is no that could be the no main calculate the ")
print(content)  

f = open("myfile.txt",'w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)

f.close()

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()

f = open('myfile.txt','r')
i = 0 
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])

  print(f"marks of student {i} in maths is : {m1*2}")
  print(f"marks of student {i} in maths is : {m2*2}")
  print(f"marks of student {i} in maths is : {m3*2}")
print(line)






