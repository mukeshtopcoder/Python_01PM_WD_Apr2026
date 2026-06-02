"""
   *
  ***
 *****
*******
 *****
  ***
   *

n = 1
m = 1
while n>0:
    for k in range(4,n,-1):
        print(' ',end="")
    for i in range(1,n*2):
        print("*",end="")
    print()
    n = n+m
    if n==4:
        m = -1

27. Create a function to sort a list without using built-in sort().
Lets try bubble sort algorithm

li = [21,78,54,23,56,90,4,12,56,89]
for s in range(len(li)):
    for i in range(len(li)-1):
        if li[i]<li[i+1]:
            temp = li[i]
            li[i] = li[i+1]
            li[i+1] = temp
print(li)


def sortList(li):
    for s in range(len(li)):
        for i in range(len(li)-1):
            if li[i]>li[i+1]:
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp
    return li

li = [21,78,54,23,56,90,4,12,56,89]
print( li ) 
print( sortList(li) )



li = [23,78,54,23,3,45,3,54,34,5,6,676,54,34,34,56,35]
print(li)
li2 = []
for x in li:
    if x not in li2:
        li2.append(x)
print(li2)


li = [23,78,54,23,3,45,3,54,34,5,6,676,54,34,34,56,35]
print(li)
print( list( set(li) ) )


"""
li = [12,34,45,67,78,89,90,95,99]
start = 0
stop = len(li)-1
target = 40
while start<stop:
    mid = (start + stop)//2
    if li[mid]==target:
        print("Found on Index",mid)
        break
    if target>li[mid]:
        start = mid+1
    else:
        stop = mid-1
else:
    print("Element Not Found!")
