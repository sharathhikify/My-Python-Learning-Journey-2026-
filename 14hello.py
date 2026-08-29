#nested loops

name=("sharath", "bharath", "naveen","sunil")
subject=("python", "java", "c++")
for names in name:
    for subjects in subject:
        print(names, subjects)


for i in range(2,11):
    for j in range(1,11):
        print(f"{i}x{j}= {i*j}")

#python revise

print("sharath")

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a=10
b=20
print(f"a:{a}, b:{b}")
print(f"a:{b}, b:{a}")

name=input("name:")
age=input("age:")
print(f"hi {name}, you are {age} years old")
