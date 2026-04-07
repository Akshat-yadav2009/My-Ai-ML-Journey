"""GRADE CALCULATOR"""

marks=float(input("enter your Marks: "))
if marks>100 or marks<0:
      print("error") 
elif 90 <= marks <= 100:
      if marks>=97 :
        print("Grade A+")
      elif marks>=93 : 
        print("Grade A")
      elif marks>=90:
        print("Grade A-")  
elif 80 <= marks <= 89:
     if marks>=87:
       print("Grade B+")
     elif marks>=83 : 
        print("Grade B")
     elif marks>=80:
        print("Grade B-") 
elif 70<= marks <=79:
     if marks>=77 :
       print("Grade C+")
     elif marks>=73 : 
        print("Grade C")
     elif marks>=70:
        print("Grade C-") 
elif 60<= marks <=69:
     if marks>=67:
       print("Grade D+")
     elif marks>=63 : 
        print("Grade D")
     elif marks>=60:
        print("Grade D-") 
elif 50<= marks <=59:
     if marks>=57:
       print("Grade D+")
     elif marks>=53 : 
        print("Grade D")
     elif marks>=50:
        print("Grade D-") 
else:
      print("Grade F")
