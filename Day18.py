"""
Advance Python
    lambda , map , filter , reduce

lambda Expression : we can write a small definition function
using lambda expression

def cube(num):
    return num**3
print( cube(5) )

lambda expression syntax:-
function_name = lambda paramter : definition

cube = lambda num : num**3
print( cube(5) )
print( cube(4) )


checkEven = lambda num:'Even' if num%2==0 else 'Odd'
print( checkEven(19) )
print( checkEven(12) )


cube = lambda num : num**3
li = [1,2,3,4,5,6,7,8,9,10]
for a in li:
    print( cube(a) )


map (built-in function)
map can apply a method/function on a collection without itteration/loop

cube = lambda num : num**3
li = [1,2,3,4,5,6,7,8,9,10]
res = list(map( cube , li ))
print(res)


setname = lambda st : st[0:3].upper()
country = ['india','Afganistan','france','uSA','GerMany']
res = list(map(setname , country))
print(res)


checkEven = lambda num:num%2==0
li = [23,67,91,58,35,68,80,35,74]
ans = []
for x in li:
    if checkEven(x):
        ans.append(x)
print(ans)



filter (Built-in Function)
you can filter out some elements from a collection without
itteration/loop using filter


checkEven = lambda num:num%2==0
li = [23,67,91,58,35,68,80,35,74]
ans = list(filter(checkEven , li))
print( ans )


add = lambda a,b : a+b
li = [1,2,3,4,5,6,7]
res = 0
for x in li:
    res = add(res,x)
print(res)


reduce  (functools library's method)
we can convert a complete collection into a single value
using reduce method


from functools import reduce

add = lambda a,b : a+b
li = [1,2,3,4,5,6,7]
res = reduce( add , li )
print( res )



# Addition

from functools import reduce
add = lambda a,b : a+b
li = [1,2,3,4,5,6,7]
res = reduce( add , li )
print( res )


# Factorial
from functools import reduce
add = lambda a,b : a*b
li = [1,2,3,4,5,6,7]
res = reduce( add , li )
print( res )


# Maximum Value

from functools import reduce
add = lambda a,b : a if a>b else b
li = [45,89,34,12,54,789,67,34]
res = reduce( add , li )
print( res )


# WAP to add square or every even element of this list
from functools import reduce

li = [12,45,78,45,41,74,42,86]
checkEven = lambda num:num%2==0
sq = lambda num:num**2
add = lambda a,b:a+b

li = filter( checkEven,li )
li = map( sq , li )
res = reduce( add , li )
print(res)





# WAP to add square or every even element of this list
from functools import reduce

li = [12,45,78,45,41,74,42,86]

li = filter( lambda num:num%2==0 ,li )
li = map( lambda num:num**2 , li )
res = reduce( lambda a,b:a+b , li )
print(res)



# WAP to add square or every even element of this list
from functools import reduce
print(reduce( lambda a,b:a+b , map( lambda num:num**2 , filter( lambda num:num%2==0 ,[12,45,78,45,41,74,42,86] ) ) ))

"""
# WAP to add square or every even element of this list
from functools import reduce
print(reduce( lambda a,b:a+b , map( lambda num:num**2 , filter( lambda num:num%2==0 ,[12,45,78,45,41,74,42,86] ) ) ))
