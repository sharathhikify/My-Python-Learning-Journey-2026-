def marrage():
    print("yash married radhika")
marrage()

def marrage(boy, girl):
    print(boy , "married" , girl)
marrage("yash", "radhika")
marrage("darshan","jayalakshmi")

def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
table(2)
table(3)
table(4)
table(5)

def func( num):
    print(str(num)*2)
func(2)

def func( num):
    print(str(num)*2)
    print(type(str(num)*2))
func(2)

def func( num):
   return int(str(num))*2
a=100
b=func(2)
c=a+b
print(c)