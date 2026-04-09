"""loops are those funtion which help us to execute a code multiple times"""
"""two types of loops:-
For and While"""

""" for loops is based on a range """
"""while loop as long as condition is true"""

"""while loops"""

a=5
while a>=1:
    print(a)
    a-=1
print("Blast off")

"""Input=int(input("enter your number > 10: "))
while Input <=10:
    Input=int(input("try again"))"""
   
"""total=0
sum=int(input("enter your number, "))

while sum!=0:
    total+=sum
    sum=int(input("enter number, "))

print("sum",total)"""


Attempts=0
while Attempts < 3:
    password=input("enter pasword: ")

    if password=="1234":
        print("Access granted")
        break
    Attempts+=1

print("done")

user =0
while user < 5:
    password=input("enter your id, ") 
    if password=="akshat":
      print("Welcome Back")
      break
    user=user+1

print("no more attempts")

choice=0
while choice!=3:
    print("1.say hello, ")
    print("2.say bye, ")
    print("3.Exit, ")

    choice=int(input("choose"))

    if choice==1:
        print("hello")
    elif choice==2:
        print("bye")
    else:
        print("exit"
        "")

i=0
num2=int(input("give me a number "))
while i<=num2:
    print(i)
    i=i+1


"""a=int(input("enter your number , "))
while a>=0:
    print(a%10)
    a=a//10  
print(a)"""


"""for loops:-"""
for i in range(25):
  print(i)

for i in range(1,6):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(5,0,-1):
    print(i)

for ch in "hello":
    print(ch)

for i in range(1,4):
    for j in range(1,4):
        print(i*j,end=" ")
    print()

for i in range(5):
    if i==3:
     break
    print(i)

for i in [1,3,5,8,9]:
    if i%2==0:
        break
    print(i)

"""counting pattern """
i=0
for i in range(5):
    i+=1
    print(i)

"""accumulator pattern"""
total=0
for i in range(1,6):
    total=total+1
    print(i)

for i in [1,23,4,7,9]:
    if i==7:
        print("found")
        break
    

for i in range(10):
    if i%2==0:
        print(i)

"""exercise:-"""
a=10
while a>=1:
    print(a)
    a-=1

print("exlpode")

Attempts=0
while Attempts>3:
    print(input("enter you password "))
    if password=="akshat":
        print("welcome back")
        break
    else:
        print("teri mkc nikal laude ")

