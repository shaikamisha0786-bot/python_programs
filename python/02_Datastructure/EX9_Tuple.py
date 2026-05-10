tup=(1,2,3,4,2,1,1)
print(tup.index(1))
print(tup.count(1))

#practice questions
movies=[]
mov1=input("enter 1st movie:") # can also write as:::movies.append(input("enter 1st movie:"))
mov2=input("enter 2nd movie:")
mov3=input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#   check palindrome using list             
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")    


#count using tuple
grade= ("c","d","a","a","b","b","a",)
print(grade.count("a"))
grade= ["c","d","a","a","b","b","a",]
grade.sort()
print(grade)