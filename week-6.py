def triangularFor(number):
    s = 0
    for i in range(number,0,-1):
        s = s + i 
    return s

def triangularWhile(number):
    s = 0
    while number > 0:
        s += number
        number -= 1
    return s
         
def triangularRecursive(number):
    if number == 0:
        return 0
    return number + triangularRecursive(number - 1)

print(f"Triangular {triangularRecursive(10)}")

def recursiveRange(start,end):
    if start == end + 1:
       return 
 
    print(start, end=" ")
    return recursiveRange(start+1,end)
recursiveRange(0,10)
print()

def recursiveRange2(start,end,asc):
    if asc:
        if start == end +1 :
            return
        print(start, end=" ")
        return recursiveRange2(start+1,end,asc)
    else:
        if start == end +1 :
            return
        print(end, end=" ")
        return recursiveRange2(start,end-1,asc)

recursiveRange2(0,10,True)
print()
recursiveRange2(0,10,False)
print()


def pairWise(start,end):
    if start == end:
       return 
   
    total = start + (start + 1)
    
    print(total, end=" ")
    return pairWise(start+1,end)

pairWise(0,10)
print()
