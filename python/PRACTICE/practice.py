
# #practice questions
a=int(input("a:"))
b=int(input("b:"))
print("sum=",a+b)
side=float(input("side:"))  
print("area=",side*side)  

a=float(input("a:"))
b=float(input("b:"))
print("avg=",(a+b)/2)

a=int(input("a:"))
b=int(input("b:"))
if(a>b):
    print("true")
else:
    print("false")    

p=float(input("p:"))
r=float(input("r:"))
t=float(input("t:"))
si=(p*r*t)/100
print(si)

#even or odd
num=int(input("enter the number:"))
if(num%2==0):
    print("even")
else:
    print("odd")

#greatest of 3 numbers entered by user
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third number is largest",a)   

    #multiple of 5
x=int(input("enter number:"))  
if(x%5==0):
    print("multiple of 5")
else:
    print("not a multiple")  



  ## print vowels 
Text= "the quick brown fox jumps over the lazy dog"
for i in Text:
  
  if i=="a" or i=="e" or i=="i" or i=="0" or i=="u" :
     print(i)


# To check string is palindrome or not
s=input()     
if s==s[::-1]:
   print("yes")
else:
   print("no")    


##PRACTICE QUESTIONS OF DICTIONARIES
#1
dictinary= {
    "cat": "a small animal",
    "table" :["a piece of furniture","list of facts & figures"]
}
print(dictinary)

#2
subjects={
    "python","java","c++",
    "python","javascript","java","python","java","c++","c"
}
print(len(subjects))

#3
marks={}
x=int(input("enter phy:"))
marks.update({"phys":x})
y=int(input("enter chem:"))
marks.update({"chem":y})
z=int(input("enter math:"))
marks.update({"math":z})
print(marks)

#4
values={9,"9.0"}
print(values)
#or
values={
    ("float",9.0),
    ("int",9)
}
print(values)