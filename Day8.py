"""
For Loop
    break , continue , pass , else

for i in range(1,11):
    print(i)



# break:-  It exit from the current loop
for i in range(1,11):
    if i==4:
        break
    print(i)



# break:-  It exit from the current loop
for i in range(1,11):
    print(i)
    if i==4:
        break


# break:-  It exit from the current loop
for i in range(1,11):
    if i%5==0:
        break
    print(i)



# continue:- Continue takes the cursor to the next itteration
# continue go for the next loop's itteration
# continue will skip the instruction after the continue

for i in range(1,7):
    if i==3:
        continue
    print(i)



for i in range(1,7):
    print(i)
    if i==3:
        continue



# continue:- Continue takes the cursor to the next itteration
# continue go for the next loop's itteration
# continue will skip the instruction after the continue

for i in range(1,11):
    if i%3==0:
        continue
    print(i)


# pass:- pass do nothing (pass just PASS the cursor to the next line)

for i in range(1,6):
    if i==3:
        pass
    print(i)

    

if 10>5:
    pass

print("Hello")


ELSE
#  ELSE will work with FOR
for i in range(1,7):
    print(i)
else:
    print(0)


for i in range(1,7):
    if i==4:
        break
    print(i)
else:
    print(0)

# else will work only if, FOR complete his task without any break

for i in range(1,7):
    if i==4:
        continue
    print(i)
else:
    print(0)



for i in range(1,7):
    if i==4:
        continue
else:
    print(0)


for i in range(1,7):
    if i==4:
        break
else:
    print(0)


count = 0
for i in range(1,7):
    if i==4:
        continue
    count=count+1  
else:
    count=count+1
print(count)



count = 0
for i in range(1,7):
    if i==4:
        break
    count=count+1  
else:
    count=count+1
print(count)


"""
