# __init__function

# class Student:
#     name="Amisha"
# S1=Student()
# print(S1.name)    


# class Car:
#     color="blue"
#     brand="BMW"
# car1=Car()
# print(car1.color)    
# print(car1.brand)



# default constuctor 
# class Student:
#     def __init__ (self):
#       pass



# parametarized constuctor
 
# class Student:
#      def __init__(self,name,marks):
#          self.name=name
#          self.marks=marks
#          print("adding new student in database")

# s1=Student("amisha",90)         
# print(s1.name,s1.marks)
# s1=Student("akshitha",90)         
# print(s1.name,s1.marks)

### methods ###

# class Student:
#      def __init__(self,name,marks):
#          self.name=name
# def hello(self):
#      print("hello",self.name)

# s1=Student("karan")
# print(s1.name)
# s1.hello()




# class Student:
#      def __init__(self,name,marks):
#          self.name=name
#          self.marks=marks
         
#      def welcome(self):
#           print("welcome student",self.name) 

#      def get_marks(self):
#           return self.marks

# s1=Student("karan",99)  
# s1.welcome()
# print(s1.get_marks())           



#practice Q-1


class Student:
     def __init__(self,name,marks):
         self.name=name
         self.marks=marks

     def get_avg(self):
          sum=0
          for val in self.marks:
               sum+=val
          print("avg score is",sum/3)     
             

s1=Student("amisha",[80,90,66])             
s1.get_avg()  