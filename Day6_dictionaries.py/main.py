"""What to study"""
"""it is a type of built in function in python that stores value with a uniqe key"""
"""noraml dictinary """
a={
    "student":"akshat",
    "age":16,
    "grade":"a"
}
print(a)
"""using dict() funtion"""
person=dict(name="adharika",age=16,grade="A",location="delhi" )
print(person)

profile={
    "name":"makimas.boyfriend",
    "follwer":18,
    "verified":True,

}

school={
     "student1":{"name":"akshat","age":16,"grade":"A","in_love":"yes"},
     "student2":{"name":"adharika","age":16,"grade":"A","in_love":"dont know"}
}
print(school["student1"]["name"])

"""zip()funtioin that helps to collect data in dictionary form"""

keys=["name","age","capable"]
values=["akshat",16,"yes"]

person=(zip(keys,values))
print(list(person))
"""to print this you have to use list other wise it give out like this <zip object at 0x0000022BDBF1BD00>"""

"""duplicate keys"""
oops={
    "name":"arjun",
    "name":"akshat",
    "age":16
}
print(oops)
"""in this case te last value print like in this akshat prints wrether than arjun"""

"""accesing value """
profile={
    "name":"makimas.boyfriend",
    "follwer":18,
    "verified":True,
    "when_joined":2025
}
account=[profile.get("name"),profile.get("follwer"),profile.get("verified"),profile.get("when_joined")]
print(account)

company={
    "Role":"AI/Ml engineer ",
    "which_level":"junior",
    "address":{
        "city":{
            "locatiion":"cetral park",
            "pincode":10022
        } 
    } 
}
print(company)

student={
    "name":"akshat",
    "subject":["math","physics","Ml"]
}
print(student["subject"])
print(student["subject"][2])
print(student["subject"][0])

data={"x":10}
try: 
    print([data["y"]])
except KeyError:
    print("key not found ")

"""modifying dictionays"""
akshat={"name":"adharika","age":16}
akshat["grade"]="A"
akshat["city"]="Delhi"

student={"name":"adwaita","age":16}
student.update({"grade":"A"})
print(student)

scores = {"math": 90, "science": 85, "english": 78,"average":84}
"""scores.pop("science")
print(scores)

scores.popitem()
print(scores)"""

if scores["average"]>=80:
    scores["result"]="pass"
else:
    scores["result"]="fail"

print(scores)

"""dictionary methods"""
"""keys"""
student = {"name": "Arjun", "age": 21, "grade": "A"}
print(student.keys())
for i in student.keys():
    print(i)

"""values"""
scores = {"math": 90, "sci": 85, "eng": 90}
print(scores.values())

"""item()"""
piyush = {"name": "Priya", "age": 20}
for keys,value in piyush.items():
     print(f"{keys}: {value}")


wordcount={}
wordcount.setdefault("hello",0)
wordcount["hello"]+=1
print(wordcount)

"""looping through dictionaries"""
scores = {"math": 90, "sci": 85, "eng": 78}
for i in scores.values():
    print(i)
average=sum(scores.values())/len(scores)
print(average)


student = {"name": "Priya", "age": 20, "city": "Pune"}

for keys,value in student.items():
    print(f"{keys}-->{value}")

"""to merge dicts"""

defaults = {"color": "blue", "size": 12}
custom   = {"color": "red", "font": "bold"}
merged= defaults | custom
print(merged)


names    = ["Arjun", "Priya"]
subjects = ["math", "sci"]
marks    = [[90, 85], [92, 88]]

report={}
for i,name in enumerate(names):
    report[name]={}
    for j,subject in enumerate(subjects):
        report[name][subject]=marks[i][j]

print(report)