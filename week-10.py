def divHelper(a,b):
    if type(a) != int or type(b) != int:
        raise TypeError("You can not divide any non-integer!!")
    if b == 0:
        raise ZeroDivisionError("You can not divide number to zero!!")
    if a < b:
        return 0
    
    return divHelper(a-b,b) + 1
   
def div(a,b):
    try: 
        return divHelper(a,b)
    except Exception as e:
        return e
    
print(div(12,2))
        
"""if a < 0 or b < 0:
            a = abs(a)
            b = abs(b)
            return -(div(a-b, b) + 1 )"""
    

