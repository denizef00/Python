for i in range(0,101):
    print(i)
    
for i in range(0,101,2):
    print(i)

for i in range(0,101):
    if i % 2 ==0:
        print(i)

#-------------------------------------------------------------
for i in range(0,10):
    if i == 5:
        break
    print(i) 
    
for i in range(1,10):
    if i == 5:
        continue
    print(i)

for i in range(0,101):
    if i % 2 != 0:
        continue
    print(i)
    
for i in range(0,101):
    if i % 2 != 0:
        print(i)
#----------------------------------------------------------------
number = 0
while number <= 100:
    print(number)
    number += 1
    
    
    
number = 0  
while number <= 100:
    print(number)
    number += 2
    if number == 101:
        break
    
while True:
    if number % 2 == 0:
        print(number)
    
    if number == 100:
        break
    
    number += 2

#----------------------------------------------------------------
students = ["Ahmet","Onur","Mehmet","Enes","Oğuz"]

for name in students:
    if name == "Mehmet":
        print(name," : ", 100)
        continue
    print(name, " : ", 50)
    
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j}=  {i * j}", end="\t")
    print()

#--------------------------------------------------------------------
number1 = 1
while number1 < 6:
    number2 = 1
    while number2 < 6:
        print(f"{number1} x {number2} = {number1* number2}", end="\t")
        number2 += 1
    print()
    number1 += 1
    
    


