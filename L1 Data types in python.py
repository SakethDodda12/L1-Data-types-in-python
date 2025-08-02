a = 5
print("type of a: ", type(a))
b = 2.5
print("type of b: ", type(b)) 
c = "coding"
print("type of c: ", type(c))
d = True
print("type of d: ", type(d)) 

name = "Saketh"
age = 12
is_student = True
weight = 55.4

print("Name :", name)
print("Data type is", type(name))

print("Age :",age)
print("Data type is", type(age))

print("Is a student :", is_student)
print("Data type is", type(is_student))

print("Weight :", weight)
print("Data type is", type(weight))

print("\n After Type Casting...")

age = str(age)
print(age)
print("Data Type of age is", type(age))

weight = int(weight)
print(age)
print("Data Type of weight is", type(weight))

text = str(input("Enter a string "))

revtext = text[::-1]
text = revtext

print("reverse of given string is:")
print(text)
      