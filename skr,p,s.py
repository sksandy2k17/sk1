a=["rock","paper","scissor"]
a[0]=='r'=='R'
a[1]=='p'=='P'
a[2]=='s'=='S'
T=input("enter your choice:")
import random
r=random.choice(a)
print("computer's choice:",r)
if r==T:
    print("tie")
if ("r==rock","T==scissor"):
    print("computer won")
if("r==scissor","T==paper"):
    print("computer won")
if ("r==paper","T==rock"):
    print("computer won")
else: print("you won")
