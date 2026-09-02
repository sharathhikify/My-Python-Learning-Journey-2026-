names=["sharath","bharath","charan"]
marks=[25,50,75]
student_marks={}
for i in range(len(names)):
    student_marks[names[i]]=marks[i]
print(student_marks)

l=[x for x in range(1,11)]
dl=[x*2 for x in l]
print(dl)

l=[x for x in range(1,11)]
dl=[x*2 for x in l if x%2==0]
print(dl)

names=["sharath","bharath","charan"]
dl={name:len(name) for name in names  }
print(dl)

names=["sharath","bharath","charan"]
dl={name:len(name)+1 for name in names  }
print(dl)

city_population={  
 "banglore":100,
 "mumbai":50,
 "hydrabad":30 
}

large_city={key:value for key,value in city_population.items() if value>=50}
print(large_city)

x=[int(num) for num in input("enetr list of integers :").split()]
print(x)

for i in range(2000,2027):
    print(f"i was born in {i},my age is {2026-i} years old")


