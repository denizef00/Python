"""
grade  ={
    "Sefa" : 100,
    "Egemen" : 100,
    "Ali" : 0,
    "Egemen" : 50
}
print(grade)

for key in grade.keys():
    print(f"{key}\t{grade[key]}")
    
for item in grade.items():
    print(f"{item[0]}\t{item[1]}")
    

for key,value in grade.items():
    print(f"{key}\t{value}")
"""

grade  ={
    "Sefa" : {
        "Quiz 1" : 50,
        "Quiz 2" : 70,
        "Assigment" : 100
        },
    "Ali" : {
        "Quiz 1" : 100,
        "Quiz 2" : 100,
        "Assigment" : 100
        }
}
#Quiz 20 Assigment 60

for keys,values in grade.items():
    s = 0
    for k,v in values.items():
        if k== "Quiz 1" or k == "Quiz 2":
            s = s + (v * 0.2)
        elif k == "Assigment":
            s = s + (v * 0.6) 
    values["Avarage"] = s
    #values.update({"Avarage" : s})
#print(grade)


with open("grade.csv","w") as grade_file:
    grade_file.write("Name,")
    for k1,v1 in grade.items():
        key_list = list(v1.keys())
        for i in range(len(key_list)):
            if i == len(key_list)-1:
                grade_file.write(f"{key_list[i]}")
            else:
                grade_file.write(f"{key_list[i]},")
            
        break
    
    grade_file.write("\n")
    
    for k1,v1 in grade.items():
        grade_file.write(f"{k1},")
        value_list = list(v1.values())
        for i in range(len(value_list)):
            if i == len(value_list) - 1: 
                grade_file.write(f"{value_list[i]}")
            else:
                grade_file.write(f"{value_list[i]},")
                
        grade_file.write("\n")
        
import pandas as pd

data = pd.read_csv("grade.csv")
print(data)