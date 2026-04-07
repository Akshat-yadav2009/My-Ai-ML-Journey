"""What to study today
 Conditional flow control:-if/else statements
 if/Else statements are used to execute a block of code based on the condition provided. the syntax is as follows:
 if condition:
     # code to execute if condition is true
 else:
     # code to execute if condition is false
 """
"""why we use it because to validate the user input and to make decisions based on the certain conditions"""

#example 1
if 5>3:
    print("5 is greater than 3")
else:
    print("error") 

Age=17
if Age==18:
    print("you can watch adult movies ")
else:
    print("error")  

name="Rahul"
if name=="Rahul":
    print("welcome Rahul")

num=10
if num%2==0:
    print("number is even ")
else:
    print("number is odd ")


password="A1233518" 
if password=="Abc123":
    print("welcome to the system")
else:
    print("invalid password")

temp=25
if temp<30:
    print("the weather is pleasant")
else:
    print("the weather is hot")

Marks=50
if Marks>=40:
    print("you have passed in the exam")
else:
    print("you have failed in the exam better luck next time")

"""using if elif  else statements"""

Marks=85
if Marks>=85:
    print("you have scored A grade")
elif Marks>=65:
    print("you have scored B grade")
elif Marks>=45:
    print("you have scored C grade ")
else:
    print("you have failed in the exam better luck next time")

"to find the positive or neagtive number"
num=18
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")

Age=15
if Age>13:
    print("child")
elif Age>20:
    print("Teen")
elif Age>60:
    print("adult")
else:
    print("senior citizen")
    

""" why we use elif statements over multiple if statements because elif statments run code one time and mulitple if have more than 1 value
"""

"""nested if statements:-"""
Age=20
has_id=True
if Age>=18:
    if has_id:
        print("entry allowed")
    else:
        print("entry denied")    


num=11
if num>0:
    if num%2==0:
        print("the number is positive")
    else:   
        print("the number is negative") 

User="Akshat"
password="Akshat@2009"
if User=="Akshat":
    if password=="Akshat@2009":
        print("hello")
    else:
        print("user not found")



Username=input("enter your username: ")
password=input("enter you password: ")
gender=input("enter your sex:")
pastmember=input("past member yes or no:")
if Username=="akshat":
    if password=="12345":
        if gender=="male" or gender=="female":
            if pastmember=="yes" or pastmember=="no":
                print("welcome past member")
            elif pastmember=="no":
                print("welcome new member")
else:
    print("invalid username or password")