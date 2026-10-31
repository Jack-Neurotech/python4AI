# lists
age = 25
has_license = False
my_list = ["Alice", 25, age, True, has_license]

name = my_list[0]
age = my_list[1]
has_license = my_list[-3]



my_list[0] = "Dave"

my_list.append("Alice")

# adds alice to the end

my_list.remove(age)

my_list.insert(1, age)

# Dictionaries: 

person = {
 "name": "Alice",
 "age": 25,
 "city": "chicago"
}

person["name"] = "dave"
person["licence"] = True

del person["licence"]


#Tuples

empty = ()

point = (3,5)

colors = ("red", "green", "blue")

print(point[0]) 
print(colors[-1]) #blue

# sets - makes new values

empty_set = set()

numbers = {1,2,3,4,5}
fruits = set(["apple", "banana", "orange"])

scores = [85, 90,90,85,92]
unique_scores = set(scores) # 85, 90, 92





  


