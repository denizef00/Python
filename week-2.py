#This is single line comment
#print("Pyhton comments are fun") #This line just print a string



"""
bsdjkbad
snadna
"""

'''
bla bla bla bla bla
'''

lecture = "Intro to Programing I"
print(lecture)
print(type(lecture))

lecturer = "Ali"
print(lecturer)
print(type(lecturer))

number_of_students = 60
print(number_of_students)
print(type(number_of_students))

average_grade_of_quizzes = 0.2
print(average_grade_of_quizzes)
print(type(average_grade_of_quizzes))

can_they_pass = False 
print(can_they_pass)
print(type(can_they_pass))

can_they_pass= "Geçebilirler!"
print(can_they_pass)
print(type(can_they_pass))

#number1 = input("Give me the first number: ")
#number2 = input("Give me the second number: ")

#total= number1 + number2 (concatenation)

number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))

total = number1 + number2 #type casting

print("Total is " ,total)

total_of_bool = True + False #output = 1 (true= 1 and false= 0) 
bool2  = True + True #output = 2 
print(total_of_bool)
print(bool2)



a = 10 
b= 4
c="---"

mul = a * b 
rep = c * a 

float_div = a / b 
int_div = a // b
print("Mul is :" , mul)
print("Rep is :" , rep)
print("Float Division is :" , float_div)
print("Integer Division is :" , int_div)

power_of_two = 2 ** 3 
print(power_of_two)