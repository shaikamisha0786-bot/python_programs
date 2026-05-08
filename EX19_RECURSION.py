def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
show(5)    



#factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(6))


#recursive function to calc sum of first n natural numbers
def calc_sum(n):
    if (n==0):
        return 0
    return calc_sum(n-1) + n

sum= calc_sum(4)
print(sum)


#print all elements in list

fruits=["apple","banana","mango","grapes"]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print(list,idx+1)

print_list(fruits)    


