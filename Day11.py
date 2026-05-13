"""
Collection:-  List, Tuple , Set , Dictionary , String , range

Sequence Data Type:-
    List , Tuple

List:-  A list is a collection of hetreogenous (different)
elements
li = [23,56,78,95,79]

li = [23,56,78,95,79]
li = [23,'Aman',67.35,True,'A',3+8j]
li = []
li = list([54,67,89])
li = list((11,22,33))
li = list()
print( li )
print( type(li) )

List works on INDEX
forward    0,1,2,3..
backward   -1,-2,-3.
list_name[index]

li = [23,54,56,456,89]
print(li)
print( li[2] )
print( li[-2] )


List supports Slicing
list_name[start_index : stop_index : step]

li = [23,54,56,456,89,34,45,56]
print(li)
print( li[3:6:1] )
print( li[3:6:2] )
print( li[3:6] )   # step = 1
print( li[ :4] )   # start = 0
print( li[ 5: ] )
print( li[ : ] )


List can be Replicate
li = [1,2,3,4]
print( li )
print( li*3 )


List can be Traverse

li = [1,2,3,4,5,6,7,8,9,10]
for x in li:
    print(x**3)


Built-in Functions
    sum , min , max , len

li = [23,56,78,64,53,23,12,54,78]
print( li )  
print( sum(li) )
print( min(li) )
print( max(li) )
print( len(li) )
print( sum(li)/len(li) )

List's Method
    append , insert , extend

li = [1,2,3,4,5]
print(li)
li.append(99)
print(li)
li.insert(2,77)
print(li)
li2 = [11,22,33]
li.extend(li2)
print(li)

list's Method
    pop , remove , del (keyword) , clear

li = [23,45,67,78,89,36,65,45]
print(li)
li.pop()
print(li)
li.pop(2)      # pop(index)
print(li)
li.remove(89)  # remove(value)
print(li)
del li[3]
print(li)
li.clear()
print(li)


List's Method
        sort , reverse 

li = [67,23,54,65,78,89]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort( reverse=True )
print(li)


        count , index

li = [23,54,56,56,47,56,24,54]
print(li)
print( li.count(56) )
print( li.index(24) )

"""
