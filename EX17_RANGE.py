seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])


seq=range(5)
for i in seq:
    print(i)

for i in range(10):
    print(i)

for i in range(5):
    print(i)
for i in range(2,10):
    print(i)    
for i in range(2,20,2):
        print(i)

                                                                                    
# even numbers

for i in range(2,100,2):
    print(i)


#  numbers from 1 to 100
for i in range(1,101):
    print(i)


#   numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#  multiplication table of a number n   
n=int(input("enter no:"))
for i in range(1,11):
    print(n*i)


# pass statement
for i in range(5):
     pass
 
print("hello")        
                  

nums=[10,20,30,40,50]
x=40
idx=0
for el in nums:
     if(el==x):
        print("element is found at index",idx)
        break
     idx=idx+1      
count=1
while count<=100:
    print("sohel")
    count+=1



for i in range(2,101,2):
    print(i)   


n=int(input("enter the number"))
if(n%2==0):
    print("even")
else:
    print("odd")    

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
is_leap(2004)