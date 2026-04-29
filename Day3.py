"""
Python Operators

a+b  =>  a,b (operands)  ,  + (oprerator)
operator do operation on operands

1- Arithmetic Operator
    + - * / % // **

a = 7
b = 5
print( a+b )
print( a-b )
print( a*b )
print( a/b )
print( a%b )   #  % modulus (to calculate the remainder)
print( 11%4 )
print( a//b ) # // truncation/floor division (it divides and print the result after removing point/decimal value)
print( 11//4 )
print( 57//6 )
print( 2**5 ) # ** Exponential ( to calculate the power (2 to the power 5))
print( 5**3 )


2- Assignment Operator
    = , += , -= , *= etc
a = 10
a += 1   # =>    a = a+1
a *= 2   # =>    a = a*2
print(a)

3- Relational / Conditional Operator
    > < >= <= == != (Return Boolean Answer)
            Boolean => True/False

a = 7
b = 5
print( a>b ) 
print( a<b )
print( a>=b )
print( a<=b )
print( a==b )   # ==  is equal to
print( a!=b )   # !=  is not equal to

4- Membership Operatort  (check existance)
        in , not in      ( Return Boolean Answer )

a = "aman"
b = "amankumar"
print( a in b )  
print( "ankum" in b )
print( "ka" in b )
print( "ka" not in b )

a = [10,20,30]
b = [10,20,30]
print( a in b )
a = 20
print( a in b )
a = [10,20,30]
b = [10,20,[10,20,30],30]
print( a in b )

5- Identity Operator  (Check Exact Match)
        is , is not   (Return Boolean Value)

a = "aman"
b = "aman"
c = "amankumar"
print( a is b )
print( a is c )
print( a is not c )

# difference of == and is
# == is use to match the content
# 'is' is use to match the reference/address

a = [1,2,3]  # object (object always takes a new memory)
b = [1,2,3]
print( a is b )
a = 10
b = 10  # it will not take a new memory
print( a is b )

6- Logical Operator
    and , or , not

and => if both inputs are True, Then the output is True
otherwise False
a = 7
b = 5
print( a>b and a<b )
print( a>b and a<20 )
print( a>10 and a<b )


and => if both inputs are False, Then the output is False
otherwise True

a = 7
b = 5
print( a>b or a<b )
print( a>b or a<20 )
print( a>10 or a<b )

not:- not operator is also called the invertor gate/operator
not will reverse the input
not will convert True to False and vice-versa
not can accept only and only one input

a = 7
b = 5
print( a>b )
print( not a>b )
print( not False )
print( not b>a )

"""
