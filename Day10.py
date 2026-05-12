"""
Looping Programming Questions
# WAP to check a number is Palindrome
# HINT:-   121  =>  Reverse => 121   Palindrome
           123  =>  Reverse => 321   Not Palindrome

num = int(input("Enter A Number : "))  # 121
copy = num
add = 0
while num>0:
    rem = num%10
    add = add*10+rem
    num = num//10
if copy==add:
    print("Palindrome")
else:
    print("Not Palindrome")


# WAP to check a number is Armstrong
# Armstrong
# 371 => 3**3 + 7**3 + 1**3 => 27+343+1 => 371
# 153 => 1**3 + 5**3 + 3**3 => 1+125+27 => 153

num = int(input("Enter A Number : "))
copy = num
add = 0
while num>0:
    rem = num%10
    add = add+rem**3
    num = num//10
if copy==add:
    print("Armstrong")
else:
    print("Not Armstrong")

# WAP to check a number is BUZZ
HINT:-  145 => 1! + 4! + 5! => 1 + 24 + 120 => 145
5! => 5*4*3*2*1 => 120

num = int(input("Enter A Number : "))   # 145
add = 0
copy = num
while num>0:
    rem = num%10
    
    fact = 1
    for i in range(1,rem+1):
        fact=fact*i
        
    add = add+fact
    num = num//10
if add==copy:
    print("BUZZ Number")
else:
    print("Not BUZZ Number")


"""

