"""
Dictionary

dic = { 1:347 , 2:384 , 3:675 , 4:347 }
print( dic )
dic = { 1:347 , 2:384 , 2:675 , 4:347 } # value will update for duplicate key
print( dic )
print( dic.keys() )
print( dic.values() )
print( dic.items() )


Methods:-
    get , clear , update , pop , popitem

d = {1:24,2:45,3:65}
print( d )
print( d[2] )
# print( d[5] ) # it will raise an error because key 5 is not available
print( d.get(5) )  # Return None if key not found
print( d.get(5,"Not Available") )
print( d.get(3,"Not Available") )


d = {1:24,2:45,3:65}
d.clear()    # remove all items
print( d )

d = {1:24,2:45,3:65}
print( d )
d1 = {2:99,4:46,5:78,6:78}
d.update(d1)
print( d )
d.pop(5)  # it will remove value of key 5 (remove item)
print(d)
d.popitem()  # it will remove the last element/item
print( d )

    copy

d = {1:23 , 2:45 , 3:68 , 4:47}
print( d )
d1 = d.copy()
print( d1 )
d1[2] = 99
print(d)
print(d1)


String:- String is also a collection of characters/symbols
st = "wdgsjk23457($&^"

st = "amankumar"
st = ""
st = str(123)
st = "aman123@gmail.com"
print( st )

String works on INDEX
both forward and backward

st = "amankumar"
print( st )
print( st[4] )
print( st[-6] )


String can be sliced
st = "amankumar"
print( st )
print( st[2:7] )

String Support Replication

st = "amankumar"
print( st )
print( st*3 )


String supports Traversing
st = "amankumar"
print( st )
for s in st:
    print(s)


st = 'amankumar'
st = "amankumar"
st = '''
amankumar
is
my
younger
brother'''

print(st)

Built-Functions
    sum , max , min , len
a,b,c--z => ASCII Values=>  97,98,99---122
A,B,C--Z => ASCII Values=>  65,66,67---90

st = "AmanKumar"
print(st)
print( len(st) )
print( max(st) )
print( min(st) )

String's Method
    upper , lower , capitalize , title

st = "aman KUmaR"
print( st )
print( st.lower() )
print( st.upper() )
print( st.capitalize() )
print( st.title() )

    strip => remove leading and trailing extra spaces

a = " aman  "
b = "      bhanu  "
print( a )
print( b )
print( a.strip() )
print( b.strip() )

    replace => replace a word/character with another
a = "I love python programming"
print(a.replace('python','java'))

# String is immuteable (You can not change anything in the string like tuple)

a = "I love python programming"
print(a.replace('python','java'))
print( a )  # it will print as it is, without any change

    split => split will seprate the words (delimeter space by default)
st = "I Love Java Programming"
li = st.split()
print( li )
li = st.split("Java")
print( li )

    join
st = "PYTHON"
print( '$'.join(st) )
li = ['I','Love','Python']
print( ' '.join(li) )  

isdigit , isnum , isalnum , isspace , startswith , endswith etc

"""
st = "aman\\nkumar"
print(st)
