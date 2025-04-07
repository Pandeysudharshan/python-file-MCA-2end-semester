from ast import Break


n1=float(input("enter first no:-"))
n2=float(input("enter second no:-"))
op=str(input("enter operation:-"))
if op=="sum":
    print("sum = ", n1+n2)

elif op=="sub":
    print("substraction = ", n1-n2)

elif op=="mul":
    print("multpliction = ", n1*n2)

elif op=="dev":
    print("deviton= ", n1/n2)

else:
    print("invalid move")

Break
    
