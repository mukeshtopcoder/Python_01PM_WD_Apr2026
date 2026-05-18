"""
SET:- Set is also a collection of unique hetregenous elements
Syntax:-
set_name = {ele1,ele2,ele3..}


Ways to create a SET

s = {23,45,56,89}
s = {23,45.78,'Aman',True}
s = {1,2,3,4,4,3,2,2,1,1,2,2,3,3,2,3}
s = {3,56,67,45,324,34,34,45,67,56,78}
s = set()
s = set([23,56,46,87,54,34])
s = set((23,56,46,87,54,34))
print(s)
print( type(s) )


SET has no INDEX
SET can not be sliced
SET can not be replicate
But, Set can be Traversed

s = {2,45,67,45,2,78,879,63}
print( s )
for a in s:
    print(a)

Built-in functions
    max, min , len , sum

s = {2,45,67,45,2,78,879,63}
print( s )
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )

SET's Method
    add , update , pop , remove , clear , discard

s = {4,56,67,42,65}
print(s)
s.add(99)
print(s)
s1 = {11,22,33,56}
s.update(s1)
print(s)
s.pop()
print(s)
s.remove(99)
print(s)
# s.remove(101)  # error because 101 key is not in the set
s.discard(11)
print(s)
s.discard(101)
print(s)
s.clear()
print(s)

Methods
    intersection , union , difference , symmetric_difference

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1.intersection(s2) )
print( s1.union(s2) )
print( s1.difference(s2) )  #-> 1235 - 234 => 15
print( s1.symmetric_difference(s2) ) # 1235 - 234 => 154


SET's opertor

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1&s2 ) # intersection
print( s1|s2 ) # Union
print( s1-s2 ) # difference
print( s1^s2 ) # symmetric_difference


Dictionary:- Dictionary is a collection of key:value pairs

d = {1:23,2:56,5:78,'Aman':890,7:754}
print( d )
print( type(d) )


d = {1:23,2:56,5:78,'Aman':890,7:754}
print( d )
print( d[5] )
print( d['Aman'] )
print( d[754] )  # throw an exception (KeyError: Not Found)


Dictionary has no index, it works on Key
Key can not be duplicate
Value can be duplicate
Its not compulsory, key should be contiguous
Dictionary can not be sliced
But, Dictionary can be Traverse

dic = {1:23,2:456,3:567,4:63,5:57}
print( dic )
for a in dic:  # by default keys will be traverse
    print(a)

Dictionary's Method
    keys , values , items

dic = {1:23,2:456,3:567,4:63,5:57}
print( dic )

for a in dic.keys():
    print(a)
    
for a in dic.values():
    print(a)


dic = {1:23,2:456,3:567,4:63,5:57}
print( dic )

for a in dic.items():
    print(a)



dic = {1:23,2:456,3:567,4:63,5:57}
print( dic )

for k,v in dic.items():
    print(k , v)


"""
