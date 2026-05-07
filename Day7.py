"""
Looping:- 
Loop:- is use to perform/execute a task again n again
for a finite times

FOR , WHILE
for
Syntax:-
for variable_name in range(start,stop,step):
    statement

# range is a collection
print( *range(1,5,1) )
print( *range(1,11,1) )
print( *range(2,21,2) )

Example
for a in range(1,5,1):
    print("Hello")


for a in range(1,11,1):
    print(a)


for a in range(2,22,2):
    print(a)

# Print Table of A Number

num = int(input("Enter A Number: "))
for a in range(1,11,1):
    print(a*num)



for i in range(1,7,1):
    print(i)


for i in range(1,7,2):
    print(i)


# By default step = 1
for i in range(1,7):
    print(i)


# By default step = 1
for i in range(5,9):
    print(i)



# By default step = 1
# By default start = 0
for i in range(5):  # if only one value (consider stop value)
    print(i)


for i in range():  # raise an error (required at least one value) 
    print(i)


# WAP to print counting from 1 to 10

for i in range(1,11):
    print(i)


# WAP to print counting from 1 to N (user input)
n = int(input("Enter A Number: "))
for i in range(1,n+1):
    print(i)


# WAP to print factors of a number.
# HINT:-   12 =>  1,2,3,4,6,12

n = int(input("Enter A Number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)


# WAP to count the factors of a number
# HINT:-  12 => 1,2,3,4,6,12 => 6 factors

count = 0
n = int(input("Enter A Number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count=count+1
print("Total Factors :",count)


# WAP to check an entered number is Prime or Not

count = 0
n = int(input("Enter A Number: "))
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")

"""
