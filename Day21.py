"""
Error:- A mistake in your code
Types of Error
1. SyntaxError
A error in your code which will be flaged by interpreter
and it will not let run the code

print("Hello')  # start " end '
a = 10
print("Hello"a)  # put a comma

You have to fix them, you can not bypass

2. RuntimeError
An error in your code that a interpreter can not flaged,
program will execute properly, but it can be crash at the
run time.

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("Division :",a/b)
print("Program Completed!")

If the denomitor is 0, it will crash the program
But, you can bypass/Handle this error at runtime
runtime error is also called Exception

3. SymmetricError   
This error can not flaged by interpreter and it will
not crash the runtime environment but you wil not
get the desired output.

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("Addition :",a*b)    # Bug
print("Program Completed!")

# You need to fix the Bug

Topic: Exception Handling
    try , except , finally

try:
    write your code here, where you have some doubt
except:
    alternate code for your error


a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except:
    print("Division is not possible")
print("Program Completed!")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except:
    print("Division is not possible")
print("Program Completed!")


a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
print("Program Completed!")


Nested except

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
print("Program Completed!")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
print("Program Completed!")


Exception class is the mother class of every exception classes

try:
    doubtful code
except:
    alternate code
finally:
    it will execute always


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
finally:
    print("Ye to hamesha chalega")
print("Program Completed!")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
finally:
    print("Ye to hamesha chalega")
print("Program Completed!")


else with exception handling
try:
    doubtful code
except:
    alternate code (it will execute if there is an error)
else:
    it will execute if there is no error
finally:
    it will execute always


a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
else:
    print("Division Complete!")
finally:
    print("Ye to hamesha chalega")
print("Program Completed!")

"""
