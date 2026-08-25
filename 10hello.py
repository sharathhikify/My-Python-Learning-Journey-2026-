#if-elif-else

import time


x=20
if x>=18:
    print("adult") 

x=24
if x%2==0:
        print("even number")
else:
        print("odd number")

x=23
if x%2==0:
     print("even number")
else:
    print("odd number")

timings="6AM"
if timings=="6AM":
    print("wakeup time and fresh up")
elif timings=="8AM":
    print("have breakfast")
else:
    print("go to college")

timings=input("ENTER THE TIME: ")
if timings=="6AM":
    print("wakeup time and fresh up")
elif timings=="8AM":
    print("have breakfast")
else:
    print("go to college")