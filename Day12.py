"""
Tuple:- Tuple is also a collection of hetregenous elements
like list.
Syntax:-
t = (34,45,67,89,86)

Ways to create a tuple
t = (23,45,56,78,90)
t = (34,67.34,True,'Aman',3+8j)
t = ()
t = tuple([23,45,56,78,89])
t = tuple((23,45,56,78,87))
t = tuple()
print(t)
print( type(t) )


Tuple works on INDEX
forward (0,1,2,3,..), backward (-1,-2,-3,..)
tuple_name[index]

t = (23,45,56,78,90)
print(t)
print( t[2] )
print( t[-4] )


Tuple can be sliced
tuple_name[start:stop:step]

t = (23,45,56,78,90)
print(t)
print( t[2:4:1] )
print( t[2:4] )
print( t[:4] )
print( t[3:] )
print( t[:] )


Tuple can be Replicate
t = (23,45,56,78,90)
print(t)
print( t*3 )

Tuple can be Traverse
t = (23,45,56,78,90)
print(t)
for x in t:
    print(x)

Built-in functions
    sum , max , min , len

t = (2,45,6,89,5)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))


Tuple's Methods
    count , index

t = (23,45,67,78,45,56)
print( t )
print( t.count(45) )
print( t.index(78) )
print( t.index(45,2) )  # (value,start_index)


Tuple is immuteable (You can not change anything in the tuple)
Tuple is faster than the list because of its immuteablity


Nested List/Tuple

li = [23,34,45,56,78]
li = [[34,45,67],3,54,67,[45,56,67]]
t = (34,56,78,45)
t = (23,45,(34,546,67),[456,778],'Aman')


li = [23,45,[4,5,678],45]
print(li)
print( li[2] )
print( li[2][2] )


List Comprehension
li = [ x for x in range(1,11) ]
li = [ x for x in range(2,21,2) ]
li = [ x**3 for x in range(1,11) ]
li = [ x if x%2==0 else 'odd' for x in range(1,21) ]
print(li)


t = (32,43,[44,55,6],76)
t[2].append(99)
print( t )



add = 0
t = (33,56,67,86,76)
print( t )
for x in t:
    add=add+x
print(add)


t = (33,56,67,86,76)
a = t[2]
for x in t:
    if x>a:
        a = x
print(a)

"""
