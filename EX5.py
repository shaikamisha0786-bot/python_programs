#sinle line if / ternary operator

# <var>=(false_val,true_val)[<condition>]
#example 1

age=int(input("age:"))
vote=("yes","no")[age>=18]

#example 2 
sal=float(input("sal:"))
tax=sal(0.1,0.2)[sal<=50000]
print(tax)

# example 3
food=input("food:")
eat="yes"if food=="cake"else "no"
print(eat)

#example 4
food=input("food:")
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")