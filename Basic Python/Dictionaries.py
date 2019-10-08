
student = {'Name': 'John', 'Age': 25 , 'Courses':['Math', 'Computer']}
student['phone'] = '+91-8971828900'
student['Name'] = 'Sathya'

print(student)

#Methods

print(student.get('Name')) #True
print(student.get('Phone', 'Not Found')) # Not Found

student.update({'Name': 'Jane', 'Age': 24, 'Phone': '+91-789456132'})

print(student)

del student['Age']

print(student)

Phone = student.pop('Phone')
print(Phone)

for key, value in student.items():
    print(key, value)