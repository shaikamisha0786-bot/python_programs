
def calc_sum(a,b): #function definition;parameters
    sum=a+b
    print(sum)
    return sum
calc_sum(1,3) #function call;arguments
calc_sum(4,1)
calc_sum(4,3)
calc_sum(4,9)
calc_sum(4,7)

def print_hello():
    print("hello")

print_hello()    
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

#average of numbers
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calc_avg(2,4,5)


#To print the length of a list 
cities=["hyd","pune","chennai","MH","ap"]
heroes=["thar","ironman","spiderman"]
def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)    

#To print the elements of a list in a single line
cities=["hyd","pune","chennai","MH","ap"]
heroes=["thar","ironman","spiderman"]
def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)  
print_list(heroes)     

#factorial of a number
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)

calc_fact(6)



#converter usd to inr
def converter(usd_val):
    inr_val= usd_val *87
    print(usd_val,"USD =",inr_val,"INR")

converter(100)


def calc_func(a):
    if a%2==0:
        print("even")
    else:
        print("odd")

calc_func(2)       