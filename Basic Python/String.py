message = 'Hello World'

print(message)

#Length of string
print(len(message))

#Slicing
print(message[0:5]) #First five char
print(message[6:])  #6th to last char

#Methods
print(message.lower())
print(message.upper())
print(message.count('Hello')) #1
print(message.find('World')) #6

new_message = message.replace('World', 'Universe')
print(new_message)

#Concatination of String
greetings = 'Hello'
name = 'Sathya'

message = greetings + ', ' + name

print(message)

#Formatted string or using f string
message = f'{greetings}, {name.upper()} .Welcome!'

print(message)

