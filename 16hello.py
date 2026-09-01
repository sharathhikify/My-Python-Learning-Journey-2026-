student_marks={
    "sharath":25,
    "bharat": 50,
    "charan": 75
}
for index,(student,marks) in enumerate(student_marks.items()):
    if index%2==0:
        print(student,marks*2)
    else:
        print(student,marks*3)


students=["sharath","bharath","charan"]
marks=[25,50,75]

student_marks={}

for index, student in enumerate(students):
    student_marks[student]=marks[index]
print(student_marks)

students=["sharath","bharath","charan"]
marks=[25,50,75]

student_marks={}

for i in range(len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)

l=[1,2,3,4]
dl=[num*2 for num in l]
print(dl)

l=[1,2,3,4]
dl=[num**2 for num in l]
print(dl)