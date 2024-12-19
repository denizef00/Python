how_much = int(input("How much money do you have in your bank account? "))
real_estate = int(input("How many house fo you have in Kötekli? "))
car = input("Do you have a car? ")

threshold_money = 100000
threshold_house = 5 

if how_much > threshold_money and real_estate > threshold_house :
    if (car == "yes" or car == "Yes"):
         print("You don't have to work all day long :)")
    else:
        print("You should buy a car bro.")   
elif how_much > 50000 and (car == "yes" or car == "Yes"):
    print("You have to work one day in a week!")
else:
    print("You are so poor you have to work to live :(")    

#-----------------------------------------------------------

hp= int(input("Car hp : "))

if hp < 60 :
    print("Not give a price")
elif hp > 60 and hp <= 75: 
    print("Price: 200.000 ")
elif hp > 75 and hp <= 90 :
    print("Price : 350.000  ")
elif hp >90 and hp <= 110:
    print("Price : 500.000")
elif hp > 110 and hp <= 150:
    print("Price : 700.000")
elif hp > 150 and hp <= 200 :
    print("Price : 1.200.000")
else :
    print("Price : 2.000.000")
    