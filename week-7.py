
empty_list = []
print(empty_list)

mixed_list = ["A", 1, 1.5, True, [1,2,3]]
print(mixed_list)

nested_list = [[[[[[[[[[8]]]]]]]]]]
print(nested_list)

matrix_list= [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

print(matrix_list)

integer_list = [0,1,2,3,10,4,5] 
print(integer_list[6])
integer_list = [0,1,2,3,10,4] #index starting 0 (first item index == 0)
#print(integer_list[6]) 
print(integer_list[-1]) 
first_four = integer_list[0:4]
print(first_four)
first_four = integer_list[:4]
print(first_four)

original_list = [1,2,3,4,5,6]
new_list = original_list[:]
new_list = original_list[:5]
print(new_list)
print(original_list)

fruit = list() # or [] 
print(fruit)
fruit.append("Banana")
print(fruit)
fruit.append("Cherry")
print(fruit)
fruit.insert(1,"Stawberry")
print(fruit)
fruit.sort(reverse=True)
print(fruit)
fruit.insert(0,"Apple")
print(fruit)
fruit.reverse()
print(fruit)
print(fruit.index("Cherry"))
print(fruit.count("Cherry"))
fruit.append("Cherry")

int_list =  [1,2,3,4,5,6,7,8,9]
print(int_list[::-1])

for i in range(len(fruit)):
    print(fruit[i])

for fruits in fruit:
    print(fruits)
    
    
def my_index(the_list,the_element):
    index = 0
    
    for i in range(len(the_list)):
        if the_list[i] == the_element:
            index = i
            return index
    return "Element does not exist in the list "

#print(fruit)

def my_count(the_list,the_element):
    acc = 0
    if type(the_list) != list :
        return "You should provide a list as a first arguments"
    for element in the_list:
         if element == the_element:
             acc += 1
             return acc
    return acc         
print(fruit)
print(my_index(fruit,"Chery"))
print(my_count(fruit,"Cherry"))