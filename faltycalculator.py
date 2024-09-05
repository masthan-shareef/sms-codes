#45*3=555,   56+9=77,  56/6=4

operator=input("enter the operation you want to do:\nadd for addition\nsub for subtraction\nmul for multiplication\ndiv for division\n mod for modulo\n pow for power\n")
op1=int(input("enter the first number"))
op2=int(input("enter the second number"))
if(op1==45 and op2==3 and operator=='mul'):
    print("555")
elif(op1==56 and op2==9 and operator=='add'):
    print("77")
elif(op1==56 and op2==6 and operator=='div'):
    print("4")
elif(operator=='add'):
    result=op1+op2
    print(result)
elif(operator=='sub'):
    result=op1-op2
    print(result)
elif(operator=='mul'):
    result=op1*op2
    print(result)
elif(operator=='div'):
    result=op1/op2
    print(result)
elif(operator=='mod'):
    result=op1%op2
    print(result)
elif(operator=='pow'):
    result=op1**op2
    print(result)
