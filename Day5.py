"""
Bitwise Operator
    and  ->  &
    or   ->  |

a = 23
b = 28
print( a&b )  # 20
print( a|b )  # 31

    shift operators
        right shift operator  >>
        left shift operator   <<

a = 21
print( a>>1 )  # 10
print( a>>2 )  # 5


a = 23
print( a>>1 )  # 11
print( a>>2 )  # 5
print( a>>3 )  # 2


a = 9
print(a<<1)   # 18
print(a<<2)   # 36

a = 4
print(a<<1) # 8
print(a<<2) # 16
print(a<<3) # 32


NOT  ( ~ )
    -(x+1) 

a = -5
print( ~a )


# ----------------------------------------------

Python Data Type

Number
    int (integer)  do not support point/decimal values
        45 , 78 , -435 , 76
    float (decimal values)
        34.456 , -23.57 , 546.0 etc
    binary ( binary number has only 2 digits 0 and 1 )
        0b101011
        a = 0b1001
        a = 0b101010111
        a = 0b10101
    Octal Number ( 0,1,2,3,4,5,6,7 )
    0o253 , 0o367
    Hexadecimal Number ( 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F )
    0x254 , 0x1FA , 0x3DCA
    Complex Number    ( a+jb )
        3+7j , 5+8j
    a = 3+7j 
    print( a )
    print( a.real )
    print( a.imag )
print( a )


String
    'A' , "Aman" , "A" , 'Aman'  # for one line
    a  = "347537434"  
    a = '''jdbjdf'''
    a = '''tyiher
    kjdfgsdjkfbjsdf      for multiple lines
    dfdsvfkhsdf
    sdfhvdskjfsd
    fsdvfkjsdf
    sdjkfsdkjf
    '''

    
Boolean
    True , False

Sequence Data Type
    List , Tuple
    li = [23,5,6,78]
    t =  (423,54,67,89,23)
    
Hash Table's Type
    Set , Dictionary
    s = {34,54,67,89}
    d = {1:345 , 2:64 , 3:67}


print( True + True*False )  
# 1 + 1*0
# 1+0
# 1   

"""
