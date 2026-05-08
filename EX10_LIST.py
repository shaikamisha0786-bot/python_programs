marks=[95.4,24.5,67.8,56.7,98.3]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student=["amisha",95.0,19,"hyd"]
print(student)
student[0]="alex"
print(student)

#list slicing
marks=[85,94,76,63,48]
print(marks[1:4])
print(marks[0:])
print(marks[:4])
print(marks[1:len(marks)])

#list methods
list=[2,1,3]
print(list.append(4))
print(list.sort())
print(list.insert(1,5))
print(list.remove(3))
print(list.pop(2))
print(list)
