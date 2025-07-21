def myAbs(num):
    if num < 0: 
        return -num
    else:
        return num


absValue = myAbs(5)
print(absValue)

def equal(x,y,z,t,a):
    if x == y or x == z or x== t or x==a or y == z or y == t or y ==t or y == a or z == t or z == t or z == a or t == a:
        return "Your number have at least two numbers"
    else:
        return "There is no equal number in that number"   

print(equal(1,2,3,4,5))
print(equal(1,1,3,4,5))
print(equal(1,1,1,4,5))
print(equal(1,1,1,1,5))
print(equal(1,1,1,1,1))

print("a","b")
print(1,2)

print("a"+"b")
print(1+2)
print("1"+"2")


a = "A"
b = "B"
print(a +" "+ b)


number1 = 5
number2 = 4
total = number1 + number2

notformattedString = str(number1) + "+" + str(number2) + "=" + str(total)
print(notformattedString)
formattedString = f"{number1} + {number2} = {total}"
print(formattedString)
secondformatted = "{} + {} = {}".format(number1,number2,total)
print(secondformatted)



#Termary Conditionals

a = 10
if a>10:
    print("Greater")

elif a > 5 :
    print(5)
else: 
    print("Smaller")

print("Greater" if a > 10 else "5" if a > 5 else "Smaller")

#---------------------------------------------------------
for i in range(10):
    if i == 9 :
        print(i)
    else:
        print(i,end=", ")
#-------------------------------------------------
x = 10

def my_function():
    global x
    print("Global x: ", x)
    x = 5
    print("Inside function:", x)


def my_function2(param):
    param = 6
    return param
my_function()      
x = my_function2(x)

print("From my function2: ", my_function2(x))
print("Outside function:", x) 


def greeting(id, name = "Guest",age = 17 ):
    print(f"Hello {name}!")
    print(f"You are {age} years old.")
    print(id)
    
greeting(id = 100 , age = 45 ,name="Deniz")

def my_func(number1,number2,name):
    total = number1 + number2
    print(f"Total is {total} {name}")

my_func(name = "Ali",number1 = 12,number2 = 12)


def greet(name):
    """
    This function greets the person whose name is passed as an argument.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    None
    """
    print(f"Hello, {name}!")

print(greet.__doc__)

