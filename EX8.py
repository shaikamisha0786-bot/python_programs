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