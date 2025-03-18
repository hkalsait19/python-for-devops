# Global and Local variables

# Global

a=10
b=20

def add():
    print(a+b)

add()

# Local

def add():
    a=11
    b=22
    print(a+b)

add()


# Mix Global & Local

a=100 #global
b=200

def add():
    print(a+b)

def sub(): #local
    c=1
    print(b-a+c)

add()
sub()