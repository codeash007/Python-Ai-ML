#lamda funciion



add = lambda a, b: a + b

# Subtraction
sub = lambda a, b: a - b

multiply = lambda a, b: a * b


divide = lambda a, b: a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))





#type function
x = 5
print(type(x))

#append function
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#extend function
my_list.extend([5, 6])
print(my_list)

#insert function
my_list.insert(2, 10)
print(my_list)

#remove
my_list.remove(1)
print(my_list)


#dictionary
my_dict = {"name": "Ashish", "age": 25, "city": "New York"}
print(my_dict)

#keys
print(my_dict.keys())   

#Values 
print(my_dict.values())   

#items
print(my_dict.items())

#GET
print(my_dict.get("name"))

#clear
my_dict.clear()

#print the cleared dictionary
print(my_dict)


#update
my_dict.update({"name":"Ashish", "age": 30, "city": "lost"})
print(my_dict)

