#conditional statements
#example 1

age=int(input("age:"))
if(age>=18):
  print("eligible to vote")
else:
   print("not eligible to vote")



#example 2
light=input("light:")
if(light=="red"):
  print("stop")
elif(light=="yellow"):
  print("look")
elif(light=="green"):
  print("go")
else:
     print("light is broken") 
    

#   #example 3
#   #nested if

age=int(input("age:"))  
if(age>=18):
       if(age>=80):
          print("can drive")
       else:
          print("cannot drive")  

else:
     print("cannot vote")        




# grades of students
marks=int(input("marks:"))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90): 
    print("B")   
elif(marks>=70 and marks<80):
    print("C")    
else:
    print("D")   

#practice 
A =int(input("A:"))   
G =input("M/F:")
if((A==1 or A==2) and G=="M"):
   print("fee is 100")
elif(A==3 or A==4 or G=="F"):   
   print("fee is 200")
elif(A==5 and G=="M"):
   print("fee is 300")   
else:
   print("no fee")   










