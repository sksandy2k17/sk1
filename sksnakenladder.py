count=0                               #assign value for count
while count<100:                      #open while loop
    roll=input("press r to roll a dice") #to roll the dice
    if roll=='r': 
        import random
        s=random.randint(1,6)          # to get random value
        print(s)  
        count=int(count)+int(s)        #increment for variable count
    if count==8:
        print("congrats, you climbed the ladder")
        count=37
    if count==11:
        print("oops, snake bitted you")
        count=2
    if count==13:
        print("congrats, you climbed the ladder")
        count=34
    if count==25:
        print("oops, snake bitted you")
        count=4
    if count==38:
        print("oops,snake bitted you")
        count=9
    if count==40:
        print("congrats,you climbed the ladder")
        count=68
    if count==52:
        print("congrats, you climbed the ladder")
        count=81
    if count==65:
        print("oops,snake bitted you")
        count=46
    if count==76:
        print("congrats, you climbed the ladder")
        count=97
    if count==89:
        print("oops,snake bitted you")
        count=70
    if count==93:
        print("oops,snake bitted you")
        count=64
    print("you are in:")
    print(count)
if count>=100:
    print("congrats you won the game")
