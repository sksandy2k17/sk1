a=int(input("enter the value"))   #accepting value for variable a
import random                     #importing random package
b=random.randint(1,10)            #assining vale for variable b through random package
c=int(input("enter the value"))   #accepting value for c
print("a=",a)                     #to print a
print("b=",b)                     # to print b
print("c=",c)                     # to print c
d,e,f=a,b,c                       #multiple assigment
if d>e:
    if d>f:
        print(d,"is greater than",e,"and",f)
if e>d:
    if e>f:
        print(e,"is greater than",d,"and",f)
else:
     print(f,"is greater than",d,"and",f)
