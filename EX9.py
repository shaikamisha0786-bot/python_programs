#strings concatenation &length
str1="shaik"
str2="amisha"
len1=len(str1)
len2=len(str2)
final_str=str1+" "+str2
print(str1+str2)
print(len1)
print(len2)
print(final_str)

#indexing
str="apna college"
print(str[3])
# slicing
print(str[0:5])
print(str[5:len(str)])
# slicing:negative indexing
print(str[-8:-1])

#string functions
str="i am a coder"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("o","a"))
print(str.replace("am","me"))
print(str.find("coder"))
print(str.count("c"))


#practice questions
name=input("enter ur name:")
len1=len(name)
print(len1)

str="hi , $iam the $ symbol $990"
print(str.count("$"))