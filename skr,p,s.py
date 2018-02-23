a=["rock","paper","scissor"]        #list of 'a' 
a[0]=='r'=='R'                      
a[1]=='p'=='P'
a[2]=='s'=='S'
T=input("enter your choice:")       #to accept the user choice
import random                       #to import random package
r=random.choice(a)                  #to pick random choice from list 'a'
print("computer's choice:",r)       #to print random choice
if (r==T):                          #start of else-if loop and checks conditions
    print("tie")
elif (r==a[0],T==a[2]):
    print("computer won")
elif(r==a[2],T==a[1]):
    print("computer won")
elif (r==a[1],T==a[0]):
    print("computer won")
else: print("you won")
