"""
Control Statements
if , if_else , Nested if_else , elif , Complex Condition
Looping:-  for , while loop

IF
Syntax:-
if condition:
    True_Statement

if 10>5:
    print("Hello India")


if 10>50:
    print("Hello India")


if 10>5:
    print("Hello India")
print("World")



if 10>50:
    print("Hello India")
print("World")



IF_ELSE
Syntax:-
if condition:
    True_Statement
else:
    False_Statement
    


if 10>5:
    print("Hello")
else:
    print("Bye")



if 10>50:
    print("Hello")
else:
    print("Bye")



# WAP to find greater value b/w two

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
if a>b:
    print("Greater Value :",a)
else:
    print("Greater Value :",b)


# WAP to check an entered Number is Even/Odd

num = int(input("Enter A Number : "))
if num%2==0:
    print("Even")
else:
    print("Odd")



Nested IF_Else
Syntax:-
if condition:
    if condition:
        True_Statement
    else:
        False_Statement
else:
    if condition:
        True_Statement
    else:
        False_Statement


# WAP to check A number is Positive, Negative or Zero

num = int(input("Enter A Number : "))
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")


# WAP to check an entered character is Vowel/Consonant
HINT:- A,E,I,O,U

ch = 'I'
if ch=='A':
    print("Vowel")
else:
    if ch=='E':
        print("Vowel")
    else:
        if ch=='I':
            print("Vowel")
        else:
            if ch=='O':
                print("Vowel")
            else:
                if ch=='U':
                    print("Vowel")
                else:
                    print("Consonant")

else:
    if
ELIF

ch = 'Z'
if ch=='A':
    print("Vowel")
elif ch=='E':
    print("Vowel")
elif ch=='I':
    print("Vowel")
elif ch=='O':
    print("Vowel")
elif ch=='U':
    print("Vowel")
else:
    print("Consonant")


Complex Condition (write all conditions together using logical operator)

ch = 'M'
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")



ch = 'W'
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")

# input return string value   
"""

a = int( input("Enter A Number: ") )
b = int( input("Enter B Number: ") )
print( a+b )
