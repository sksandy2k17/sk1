marks=int(input("enter the marks obtained:"))   #aacpets the mark and converts to integer
if marks>90:                                    #start of else-if loop
    print("garde A")
elif marks>80:
    print("grade B")
elif marks>65:
    print("grade C")
elif marks>=45:
    print("grade D")
else:
    print("fail")
