def add(x,y):                  #funtion definition
    return x+y                 #returns value if the function is called
def sub(x,y):       
    return x-y 
def mul(x,y):
    return x*y
a=int(input("enter the value"))  #assings the value
b=int(input("enter the value"))
print("add of 2nos is",add(a,b))  #calls the funtions and to print
print("sub of 2 nos",sub(a,b))
print("mul of 2 nos",mul(a,b))
print("minimum value u entered",min(a,b))    
print("maximum value you entere",max(a,b))
