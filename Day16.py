"""
24. Check whether a triangle is equilateral, isosceles, or scalene

s1 = 10
s2 = 20
s3 = 30
if s1==s2==s3:  #  s1==s2 and s2==s3
    print("Triangle is Equilateral")
elif s1==s2 or s2==s3 or s3==s1:
    print("Triangle is  isosceles")
else:
    print("Triangle is scalene")

26. Calculate electricity bill using slab-wise rates.

units = 500
service = 200
if units<100:
    amt = service + 5*units
elif units<200:
    amt = service + 4*units
elif units<300:
    amt = service + 3*units
else:
    amt = service + 2*units

print("total bill :",amt)


29. Find the second largest number among three numbers

a = 1000
b = 200
c = 30
if (a>b and a<c) or (a<b and a>c):
    print("Second Largest :",a)
elif (b>a and b<c) or (b<a and b>c):
    print("Second Largest :",b)
else:
    print("Second Largest :",c)



Using nested if else

a = 100
b = 20
c = 3000
if a>b:
    if a>c:
        if b>c:
            sec = b
        else:
            sec = c
    else:
        sec = a
else:
    if b>c:
        if a>c:
            sec = a
        else:
            sec = c
    else:
        sec = b
print("Second Largest :",sec)


"""

