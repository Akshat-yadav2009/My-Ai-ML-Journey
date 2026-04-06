"""what to study
1)operators
2)Input/output"""

"""operators
1)Arithmetic operators: +, -, *, /, %, **
2)comparison operators: ==, !=, <, >, <=, >=
3)Logical operators : and or not"""

"""Addition"""
price1=100
price2=350
total=price1+price2
print(total)

"""common mistake in addition:-strings can be concatenated instead of added"""

"""subtraction """
A=50
B=20
gap=A-B
print(gap)

""" common mistake in subtraction:-smaller one can be subtracted from larger one and python won't give any error """

"""multiplication"""
Ak=30
AD=20
total=Ak*AD
print(total) 

"""common mistake in multiplication:-When int*float it gives float and even its a whole number it will float """

"""division"""
D=100
d=20
result=D/d 
print(result)

"""In division answer is always float"""

"""floor division"""
F=100
f=20
result=F//f 
print(result)

"""common mistake in floor division :- when X//y it roundes to the nearest integer like 7//2 gives 3 but -7//2 gives -4"""

"""modulus operator"""
Y=50
y=10
result=Y%y
print(result)

"""exponentiation operator"""
X=5
y=3
result=X**y
print(result) 

"""to find a square root of number without using a function"""
num=16
sqrt=num**0.5
print(sqrt) 

print(10/3)

"""Comparison operators"""
a=5
b=10
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

"""logical operators """
"""And operator if both are true the its true else it is false"""
Age=20
Has_id=True

print(Age>18 and Has_id)
print(Age>=18 and Has_id)
print(Age<18 and Has_id )

"""or operator if one of the condition is true then its true else it is false"""

This_weekend=True
is_holiday=False

print (This_weekend or is_holiday)
print( False or is_holiday)

"""not operator it gives the opposite of the condition"""

Raining=True
print(not Raining)
print(not True)
print(not(5>3))

"""input() funtion is used to take input from the user and it always returns a string"""

 
Age=int((input("enter your age")))
print(type(Age))

height=float(input("enter your height, ")) 
print(type(height))

age=int(input("enter your age,"))
print("next year you will be", age + 1)

name="akshat"
CLASS="12th"
maths_marks=85
 
print("="*20)
print(f"Name:{name}\nCLASS:{CLASS}\nmaths_marks:{maths_marks}")
print("="*20)