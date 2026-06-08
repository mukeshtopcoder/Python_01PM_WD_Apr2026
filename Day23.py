"""
File Handling
Binary File ( .dat , .bin etc )
Binary file stores data in the form of object and in encoded format

file_handler = open('file_name.extension' , 'mode')
mode :-  rb , wb , ab , rb+ , wb+ , ab+

to write data in a binary file we need pickle module
dump => dump is use to write some data in a file
load => load is use to read the data from a file

import pickle
file = open('employee.bin','wb')
pickle.dump('Ramesh Singh',file)
file.close()


import pickle
file = open('employee.bin','ab')
pickle.dump('Mohit Agarwal',file)
file.close()


import pickle
file = open('employee.bin','rb')
data = pickle.load(file)  # read only one object
print(data)
file.close()


import pickle
file = open('employee.bin','rb')
data = pickle.load(file)
print(data)
data = pickle.load(file)
print(data)
data = pickle.load(file)
print(data)
file.close()


import pickle
file = open('employee.bin','rb')
for i in range(3):
    data = pickle.load(file)
    print(data)
file.close()


"""
import pickle
file = open('employee.bin','rb')
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("Read Complete")
file.close()
