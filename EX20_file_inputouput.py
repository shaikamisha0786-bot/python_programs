#reading a file

f= open("demo.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
data= f.read()
print(data)
f.close()


#writing a file
f=open("demo.txt","w")
f.write("\n hello this is me")

#appending a file"
f=open("demo.txt","w")
f.write("\n hello this is me")


with open("demo.txt","r") as f:
    data=f.read()
    print(data)
    
with open("demo.txt","a") as f:
    f.write("new data  this one is first")
    



import os
os.remove("sample.txt")  

#practice Q-1

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning I/O\n")
    f.write("using java.\ni like programming in java.") 


#practice Q-2
with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)    
with open("practice.txt","w") as f:
    f.write(new_data)

#practice Q-3
def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
      data=f.read()
      if(data.find(word))!=-1:
              print("word found")            
      else :
        print("word not found")

check_for_word()       


#practice Q-4   

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1
    return -1
print(check_for_line())       

#practice Q-5 
count=0
with open("sample.txt") as f:
    data=f.read()
    print(data)
    nums=data.split(",")
    for val in nums:
       if(int(val)%2==0):
           count+=1
print(count)            