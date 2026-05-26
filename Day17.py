"""
UDF:- User Defined Function
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

A function is a block of statements which perform a specific task and
return a value.

Syntax:-
def function_name(parameters):
    definition

function_name(argument)


Built-in functions  :   sum , max , min , len


def greet():
    print("Good Morning")

greet()   # calling (you want to execute this function)
greet()



def greet(name):    # name -> parameter
    print("Good",name)

greet("Morning")    # argument
greet("Noon")
greet("After Noon")
greet("Evening")



def add(a,b):
    print(a+b)

add(10,20)



def add(a,b):
    return a+b

print( add(10,20) ) 



def add(a,b):
    return a+b

res =  add(10,20) 
print( res )



def add(a,b,c):
    return a+b+c

print( add(10,20,30) )  



def add(a,b,c=0):
    return a+b+c

print( add(10,20) )  



def add(a=0,b=0,c=0,d=0,e=0,f=0):
    return a+b+c+d+e+f

print( add(34,4,56) )  



def add( *a ):    # *a => tuple     #  *args
    return sum(a)

print( add(45,45,56) )    # pass any number of arguments


def add( **a ):    #  dictionary      #  **kargs
    return a

print( add( name='rahul kumar' , course='Python Full Stack') )  



def add(a,b=0,c=0,d=0):   # you can assign the default values from right side
    return a+b+c+d

print( add(10) )  # you can assign arguments to parameter from left side



# Recursion :- Recursion is a property of a method/function where it calls itself

def hello():
    print("Hello India")
    hello()

hello()


# WAP to add all natural numbers
# Natural Number: 1,2,3,4,5....

def add(num):
    a = 0
    for i in range(1,num+1):
        a = a+i
    return a

print( add(10) )


# WAP to add all natural numbers using recursion
# Natural Number: 1,2,3,4,5....

def add(num):
    if num==1:
        return 1
    else:
        return num + add(num-1)

print( add(5) )  


 
# WAP to calculate factor of a number
# 5 => 5*4*3*2*1 => 120

def add(num):
    if num==1:
        return 1
    else:
        return num * add(num-1)

print( add(5) )  


"""
