import random


#empty_tuple = ()
empty_tuple = tuple()
casting = tuple([0,1,2,3,4,5,6,7,8,9])

#print(type(casting))

myTuple = (1,2,3,4,4,5)

#print(myTuple.count(4))
#print(myTuple.index(3))

temperatures= [12,21,34,16,7,0,19,23]
def biggest_differences(temps):
    
    max_temp = 0
    for temp in temps:
        if temp > max_temp:
            max_temp = temp
    
    max_index = temps.index(max_temp)
        
    biggest_difference = 0   
    for i in range(max_index,len(temps)-1):
        diff = abs(temps[i]- temps[i+1])
        if diff > biggest_difference:
            biggest_difference = diff
        
    return biggest_difference
        

#print(biggest_differences(temperatures))
    
    
number = random.randint(0,1000)

guess = int(input("Please make a guess between 0 and 1000: "))
counter = 1
while guess != -1 and number != guess and counter <= 9 :
    if guess > number:
        print("Number is less than your guess")
    else:
        print("Number is greater than your guess")
        
    guess = int(input("Please make a another guess: "))
    counter += 1


if -1 == guess:
    print("Thank you for playing this game see you :(")
if number == guess:
    print("Congrast!!! You WON !!")
elif counter > 9 :
    print("You lost idiot!!")            
    
    
