
#print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1
# print("ended")    

#print numbers from 100 to 1
# i=100
# while i>=1:
#    print(i)
#    i-=1
# print("ended")   


#print multiplication table of a number n 
# i=1
# n=int(input("enter the number:"))
# while i<=10:
#     print(n*i)
#     i+=1

# print the no.s
# nums=[1,4,9,16,25,36,49,64,81,100]    
# idx=0
# while idx < len(nums):
#      print(nums[idx])
#      idx+=1

#search for a number x in this tuple    
# nums=[1,4,9,16,25,36,49,64,81,100,36]    
# x=36
# i=0
# while i< len(nums):
#      if(nums[i]==x):
#           print("found at idx",i)
#           break

#      else:
#          print("finding...")     
#      i+=1
# print("end of loop")

#break 
# i=0
# while i<=5:
#      print(i)
#      if(i==3):
#           break
#      i+=1
# print("end of loop")

#continue
# i=0
# while i<=5:
#      if(i==3):
#           i+=1
#           continue
#      print(i)
#      i+=1


#odd
# i=1
# while i<=10:
#      if(i%2==0):
#           i+=1
#           continue  #skip
#      print(i)
#      i+=1

#  #even
# i=0
# while i<=10:
#      if(i%2!=0):
#           i+=1
#           continue
#      print(i)
#      i+=1    

#sum of first n numbers
# n=5  
# sum=0   
# for i in range(1, n+1):
#      sum +=i
     
# print("total sum=",sum)

#factorial of first n numbers
n=5
fact=1
i=1
while i<=n:
     fact *=i
     i+=1
print("factorial=",fact)     