"""
Pattern Programming

*****
*****
*****
*****
*****



print("*****")
print("*****")
print("*****")
print("*****")
print("*****")


print("*****\n*****\n*****\n*****\n*****\n")

print("*****\n"*5)

for i in range(5):
    print("*****")


# column

*****   # row
*****
*****
*****
*****


for i in range(1,6):  
    for j in range(1,6):    
        print("*",end='')
    print()


*
**
***
****
*****

for i in range(1,6):  
    for j in range(1,i+1):    
        print("*",end='')
    print()


1
12
123
1234
12345


for i in range(1,6):  
    for j in range(1,i+1): 
        print(j,end="")
    print()


1
22
333
4444
55555


for i in range(1,6):
    for j in range(1,i+1):  
        print(i,end="")
    print()


1
23
456
78910

k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()

1
23
456
7890

0
12
345
6789

k = 0
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()


k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k%10,end="")
        k=k+1
    print()


A
AB
ABC
ABCD
ABCDE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()

A
BB
CCC
DDDD
EEEEE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(i+64),end="")
    print()


A
BC
DEF
GHIJ
KLMNO

k = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end="")
        k=k+1
    print()


    *
   **
  ***
 ****
*****

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


*
**
***
****
*****

for i in range(1,6):
    print("*"*i)

1
22
333
4444
55555

for i in range(1,6):
    print(str(i)*i)

    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(' '*(5-i),"*"*i)

    *
   * *
  * * *
 * * * *
* * * * *

for i in range(1,6):
    print(' '*(5-i),"* "*i)

1
12
123
1234
12345

st = ""
for i in range(1,6):
    st = st + str(i)  
    print(st)


0
909
89098
7890987
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321


s = '0'
for i in range(10,0,-1):
    if i!=10:
        s = str(i) + s + str(i)
    print(s)


   *
  ***
 *****
*******
 *****
  ***
   *

for i in range(1,5):
    for k in range(4,i,-1):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()
for i in range(3,0,-1):
    for k in range(i,4):
        print(" ",end="")
    for j in range(i*2-1,0,-1):
        print("*",end="")
    print()
    
"""
