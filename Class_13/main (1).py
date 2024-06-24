# string = str("hello")
# class str:
#     def __init__(self, o):
#         self.o = o
        
#     def __str__(self):
#         return o
    
    
# print(string)
# class MyClass:
#     """This is myclass class. no argument ```hi```"""
#     def __init__(self):
#         name = "John"
    
#     def __str__(self):
#         return "This is string"

# myobject = MyClass()
# print(myobject)

# print(list.count([1, 2, 3, 1], 1))

# list1 = [1, 2, 3, 1]
# print(list1.count(1))

# class Car:
#     count = 0
    
#     def __init__(self, name):
#         self.name = name
#         self.km = 0
#         Car.count += 1
        
# matiz = Car('matiz') 
# nexia = Car('nexia') 
# cobalt = Car('cobalt') 
# print(Car.count)
# print(matiz.count)

my_list = ["airflow", "tsql", "python"]
my_list = [i for i in my_list if i != "python"]
print(my_list)

