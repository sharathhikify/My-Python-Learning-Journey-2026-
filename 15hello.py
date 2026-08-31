   

l=[1,2,3,4]
t=1
for num in l:
    t=t*num
print(t)    

l=[1,2,3,4]
t=0
for num in l:
    t=t+num
print(t) 

i=[1,2,3,4]
dl=[]
for num in l:
    dl.append(num*2)
print(dl)

i=[1,2,3,4]
dl=[]
for index in range(0,len(i),2):
    dl.append(i[index]*2)
print(dl)


student_marks={"sharath":25, "bharat": 50, "navin":75}
for students, marks in student_marks.items():
    print(f"{students}: {marks}")
print (student_marks)    

student_marks={"sharath":25, "bharat": 50, "navin":75}
for index, name in enumerate(student_marks):
    if index%2 ==0:
       print(name, ":", student_marks[name])
    
    
