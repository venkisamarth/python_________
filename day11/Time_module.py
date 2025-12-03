import time 
print(time.time())

import time 
print("Start:",time.time())
time.sleep(2)
print("End:",time.time())

import time 
t = time.localtime()
formatted_time= time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)


import time 
current_time= time.strftime("%H:%M:%S")
print("Current Time:", current_time)



# mesuring the how long the time the program run 
import time 
start = time.time()
for i in range(1,100): 
    print(i)
end = time.time()

print("time take:",end- start,"seconds")

import time 
seconds= 5 
for i in range(seconds, 0,-1): 
    print(i)
    time.sleep(1)
print("Time's up!")


