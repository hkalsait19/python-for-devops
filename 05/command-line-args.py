import sys ## to importing command line args

def add():
    add=num1+num2
    print(add)

def sub():
    add=num1+num2
    print(sub)

num1=sys.argv[1] ## 1st command line argument
operation = sys.argv[2] ## 2nd command line argument
num2=sys.argv[3] ## 3rd command line argument

if operation == "add":
    output=add(num1,num2)
    print("Addition of two numbers is: ",output)