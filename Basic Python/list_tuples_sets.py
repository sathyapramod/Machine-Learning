# List

courses = ['History', 'Math', 'Physics', 'ComputerScience']
courses_2 = ['Ada', 'DS']

print(courses[0]) # First item of list
print(courses[-1]) #Last item in list

#Slicing
print(courses[0:3])
print(courses[:2])
print(courses[2:])

#append and insert method
courses.append('Art')
courses.insert(0, 'Cyber')

print(courses)

#Extend method
courses.extend(courses_2)
print(courses)

#Remove and pop methods
courses.remove('History')
courses.pop()

print(courses)

#sort lits
courses.sort()
print(courses) # Asending sort

courses.sort(reverse=True)
print(courses) #decending sort

#Enumarater
for index, courses in enumerate(courses):
    print(index, courses)


#Sets
cs_course = {'History', 'Math', 'Physics', 'CompSci'}
art_course = {'History', 'Math', 'Art', 'Design'}

print(cs_course)
print(art_course)

#Methods in Sets
print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))