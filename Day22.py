"""
    assert  (it is use for custom error)

age = int(input("Enter Age : "))
assert age>17
print("Welcome to my page!")


age = int(input("Enter Age : "))
assert age>17 , "Age Should Be 18+"
print("Welcome to my page!")



try:
    age = int(input("Enter Age : "))
    assert age>17 , "Age Should Be 18+"
    print("Welcome to my page!")
except AssertionError as e:
    print("Error :",e)


        raise  (to raise an custom Error)

age = int(input("Enter Age : "))
if age<18:
    raise ValueError("Age Should Be 18+")
print("Welcome to my page!")


age = int(input("Enter Age : "))
if age<18:
    raise ZeroDivisionError("Age Should Be 18+")
print("Welcome to my page!")


# Custom Exception Class
class AgeError(Exception):
    pass

age = int(input("Enter Age : "))
if age<18:
    raise AgeError("Age Should Be 18+")
print("Welcome to my page!")

# ==================================================
File Handling
    Text File , Binary File
Text File (.txt , .docx , .xlsx etc)
    text file store data character 
    Mohan Sharma  -> 4 Char =>   Moha
Binary File (.bin , .dat etc)
    binary file stores data in the form of object
    Mohan Sharma  -> it will read a complete object

Text file:-
file_handler = open( 'file_name.extension' , 'mode' )
mode:-  r , w , a , r+ (rw) , w+  (wr) , a+ (ar)

file = open('student.txt','w')
file.close()

# WAP to write data into  a file

file = open('student.txt','w')
file.write("Maneesh")
file.close()
# w mode -> will erase past data and write new data everytime


file = open('student.txt','a')
file.write("\nRahul Kumar")
file.close()
# a mode => it will add new data to the file without erasing old data


li = ['\nYogesh Singh','\nShiva Yadav','\nVikas Singh']
file = open('student.txt','a')
file.writelines(li) # use to write multiple data
file.close()
# a mode => it will add new data to the file without erasing old data


# WAP to read data from a file

file = open('student.txt','r')
data = file.read()  # read all data
print(data)
file.close()


file = open('student.txt','r')
data = file.read(20)  # read 20 characters
print(data)
file.close()

file = open('student.txt','r')
data = file.readline()  # read one line only
print(data)
file.close()


file = open('student.txt','r')
data = file.readline()  
print(data)
data = file.readline()  
print(data)
data = file.readline()  
print(data)
file.close()


file = open('student.txt','r')
for i in range(5):  # will work for 5 times and read 5 lines
    data = file.readline()  
    print(data)
file.close()



file = open('student.txt','r')
while True:
    data = file.readline()
    if len(data)==0:
        break
    print(data)
file.close()


file = open('student.txt','r')
data = file.readlines()
print(data)
for name in data:
    print(name)
file.close()


# tell

file = open('student.txt','r')
print( file.tell() )  # tell will display current position of the cursor
data = file.read(10)
print(data)
print( file.tell() )
data = file.read(10)
print(data)
file.close()


# seek

file = open('student.txt','r')
print( file.tell() )
file.seek(10)  # will skip 10 characters
print( file.tell() )
file.close()

"""
