print("="*40)
print("my first calculator")
print("="*40)

n1=float(input("enter your first number, "))
n2=float(input("enter your second number, "))
operation=input("choose your operation +,-,/,*,//,%,**, ") 

if operation=="+":
    print(n1+n2)

elif operation=="-": 
    print(n1-n2)

elif operation=="/":
    print(n1/n2)

elif operation=="*":
    print(n1*n2)

elif operation=="//":
    print(n1//n2)

elif operation=="%":
    print(n1%n2)
    
elif operation=="**":
    print(n1**n2)

else:
    print("invalid input")

print(f"{n1} {operation} {n2} = {eval(str(n1) + operation + str(n2))}")

print("="*40)

"""find your age and check if you can vote or not"""

Birth_year=int(input("enter your birth year, "))
current_year=int(input("enter the current year, "))
age=current_year-Birth_year
print (f"your age is {age}")

if age>=18:
    print ("you are an adult you can vote now")