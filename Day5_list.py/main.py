"""list is a catalouge which used to store multiple information in form of boolean float integer string"""
lis=[24,22,"string",True,3.14]

#creating list:
#empty list:
a=[]
#normal list:
b=[12,33,344,55]
#string list:
c=[1,"hello",3.5,True]
#nested list:
d=[[12,332,113],[33,344,233,4]]
#using list:
e=list(range(5))

"""acessing list"""
#indexing start with 0:
nunu=[10,27,20,502334,4343,43,434,34343434,433434,343434,213556,767678789,798998956,]
print(nunu[0])
print(nunu[5])
print(nunu[9])
print(nunu[5])
print(nunu[len(nunu)-1])

"""slcing in list"""
akshat=[12,-22,273,383,3838,3838 ,576,345,4656,565656334,6,34643,63463467,676789,9]
print(akshat[1:4])
print(akshat[0:9:2])
print(akshat[:3])
print(akshat[::3])
print(akshat[-4:5])
print(akshat[::-1])

"""modifying list   """
adharika=[36,24,32,12,35,5456,5676,6754,336,444]
adharika[0]=34
adharika[0:2]=[35,34]
adharika.append(6)
adharika.insert(1,100)
adharika.extend([167])
adharika.remove(167)
adharika.pop(2)
adharika.pop()
del adharika[0]
adharika.clear()
print(adharika)

"""list operators """
a=[1,2]
b=[3,4]
c=a+b
print(c)
print(c*3)
print(4 in c)
print(len(c))
print(min(c))
print(max(c))
print(sum(c))

"""looping in string"""
a=[1,2,3,4,5,6,7]
for i in a:
    print(i)
for i,x in enumerate(a):
    print(i,x)

i=0 
while i<len(a):
    print(i)
    i+=1

squares=[x*x for x in range(5)]
print(squares) 