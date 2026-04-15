"""functions:- A block of code that we created and we use it whenever we want """
def akshat():
    print("this is hello function for using hello")

akshat()

def sum(a,b):
    print(f"this is your sum of two numbers {a+b}")

sum(12,55)

def name(name):
    print(f"you name is {name}")

name("adharika")


"""key word argument"""
def hello(name,age):
    print (f"your name is {name} you age is {age}")

hello(age=16,name="adharika")

def name(name,age,grade,student_class,percentage):
    print(f"your name is {name} your age is {age} youre are studying in {student_class} your grades are {grade}, finaly your percentage is {percentage}")

name(grade="B+",name="akshat",age=16,student_class="11th",percentage="60%")
name(grade="A+",name="aadharika",age=16,student_class="11th",percentage="91%")


"""default arguments """
def adharika(a,b=45):
    print (f"you sum is {a+b}")

adharika(12)
adharika(12,18)

"temperature converter"
def temperature_converter(value,c_unit="C",f_unit="F",round_to=1):
    if c_unit=="C"and f_unit=="F":
      result = (value * 9/5) + 32  
    elif f_unit=="f"and c_unit=="c":
      result = (value - 32) * 5/9  
    else:
        value=result
        
    return round(result,round_to)

print(temperature_converter(100,"C","F"))

def describe_data(numbers, show_mean=True, show_count=True, show_range=True, show_decimal=2):
    result = {}

    if not numbers:
        return {"error": "Empty list provided"}

    if show_count:
        result["count"] = len(numbers)

    if show_mean:
        mean = sum(numbers) / len(numbers)
        result["mean"] = round(mean, show_decimal)

    if show_range:
        result["min"] = min(numbers)
        result["max"] = max(numbers)
        result["range"] = result["max"] - result["min"]

    return result


scores = [85, 92, 78, 95, 88, 76, 91]
print(describe_data(scores))
        

"arbitray arguments"
"*args:- to run multiple arguments like add(167202,22122,223,2,22112,233 type of args is a tuple )"
def add(*args):
    total=0
    for arg in args:
        total+=arg
        
    return total

print(add(12,23,34,55,667,32))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("adharika","akshat","yadav" )

"""Mixing Regular Params with *args"""

def introduction(greetings,*args):
    for arg in args:
        print(f"{greetings},{arg}")

print(introduction("fuck you","manu","yusuf","shivam"))


"""Average calculator"""
def Average_calculator(*args):
    if len(args)==0:
        return 0
    total=sum(args)
    count=len(args)
    return round(total/count,2)

print(Average_calculator(80,70,20))

def Join_words(seprator,*words):
    result=""
    for word in words:
        result+=word
        if 1<len(words)-1:
            result+=seprator
    return result

Join_words(",","you","are",)

"""**kwargs:- it helps us to give mulptiple keyword arguments"""

def display_address(**kwargs):
    for keys,values in kwargs.items():
        print(f"{keys}:{values}")
              
display_address(country="india",
                state="Delhi",
                city="New Delhi",
                pin="110018")
"""profile builder"""

def Profile(first_name,last_name,**details):

 Profile={
    "first_name":first_name,
    "last_name":last_name 
 }
 for keys,values in details.items():
        Profile[keys]=values

 return Profile


""" Config system using kwargs"""

def configure_app(**kwargs):
    defaults = {
        "debug": False,
        "port": 8080,
        "host": "localhost",
        "log_level": "INFO",
        "max_connections": 100
    }


    for keys,values in kwargs:
        if keys in defaults:
            defaults[keys]=values
        else:
            print(f"  ⚠️ Unknown setting: '{keys}' (ignored)")

    return defaults

"""lambda function"""
sqaure=lambda x:x**5
sqaure(5)

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob",   "score": 85},
    {"name": "Carol", "score": 98},
]

sorted_students=sorted(students,key=lambda s:s[scores])   

"""lambda with map()"""

prices = [10.0, 25.5, 8.99]
post_prices=list(map(lambda p:p*1.18,prices))

""" lambda with filter() """    
scores = [45, 88, 62, 71, 33, 95]
post_scores=list(filter(lambda s:s>=80,scores))

"""recursion"""
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

"""fibonacci"""
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
