"""
While Loop

initialization
while condition:
    statements
    incr/decr

Example:-
a = 1
while a<5:
    print("Hello")
    a = a+1


a = 1
while a<=5:
    print("Hello")
    a = a+1



a = 1
while a<=10:
    print(a)
    a = a+1


num = int(input("Enter A Number : "))
a = 1
while a<=10:
    print(a*num)
    a = a+1



num = int(input("Enter A Number : "))
a = 1
while a<=num:
    print(a)
    a=a+1


# WAP to print factors of a number
# HINT:-  12 => 1,2,3,4,6,12

num = int(input("Enter A Number : "))
a = 1
while a<=num:
    if num%a==0:
        print(a)
    a=a+1

# WAP to count the number of factors

count = 0
num = int(input("Enter A Number : "))
a = 1
while a<=num:
    if num%a==0:
        print(a)
        count+=1
    a=a+1
print("Total Factors :",count)


# WAP to check a Number is Prime or Not

count = 0
num = int(input("Enter A Number : "))
a = 1
while a<=num:
    if num%a==0:
        count+=1
    a=a+1
if count==2:
    print("Prime")
else:
    print("Not Prime")


While loop is used for custom conditions

ch = 'Y'
while ch in 'Yy':
    name = input("Enter Name : ")
    add = input("Enter Address : ")
    ch = input("Do You Want To Continue (Y/n) : ")


# WAP to add all digits of number
# HINT:- 273 => 2+7+3 => 12 Result

num = int(input("Enter A Number : "))
add = 0
while num>0:
    rem = num%10  
    add = add+rem  
    num = num//10  
print("Addition of Digits :",add)


# WAP to reverse a Number

num = int(input("Enter A Number : "))  
add = 0
while num>0:
    rem = num%10      
    add = add*10+rem   
    num = num//10      
print("Addition of Digits :",add)

"""
 
