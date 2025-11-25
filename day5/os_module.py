import os 
f = os.open("myfile.txt",os.O_RDONLY)
contents = os.read(f,1024)
os.close(f)
print(f)

import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")

# if (not os.path.exists("data")):
#    os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"tutorial/day{i+1}")

# if (not os.path.exists("100_days_python")):
#     os.mkdir("python")
# for i in range(0,100):
#     os.mkdir(f'python/class{i+1}')



import os 
# folders = os.listdir("data")

# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))
 

# for i in range(0, 100):
#     os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
# for i in range(0,100):
#     os.rename(f"data/tutorail{i+1}",f"data/clases {i+1}")

# if(not os.path.exists("pavan")):
#     os.mkdir("pavan")
# for i in range(1,100):
#     os.mkdir(f"pavan/class{i+1}")

for i in range(1,100):
    os.mkdir(f"pavan/class11/main.py")

for i in range(0, 100):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")






