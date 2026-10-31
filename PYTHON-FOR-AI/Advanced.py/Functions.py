def greeting():
    print("Hello")

greeting()

# functions with conditions

def check():

 x = 16
 if x > 20:
   print("hot")
 else:
    print("cool")

check()

# Parameters

def greet(first_name, last_name):
   print(f"Hello, {first_name} {last_name}")

   greet(first_name="Dave", last_name="G")

# Multiple parameters:

def calc(price, tax, discount):
   tax = price ** tax - discount 
   final_price = tax + price
   print(f"Total: ${final_price}")

calc(100, .08, 10)

# Global v. local Variables 

discount = 20 

def calculate(price):
   tax_rate = .08
   discount = 10

   tax = price * tax_rate
   final_price = price + tax - discount

   print(f"Total: ${final_price}")

calculate(price=100)



def add(a,b):
   print(a + b)

add(a =5, b =10)

def add_return(a, b):
    return a+b 

result = add_return(a=5, b=10)

result + 20 


# manipulating values

def calc(width, height):
   area = width * height
   area = area * 1.05
   return area

def double(area):
   return area *2

print(double(3))

# printing mutliple numbers

def simple_function():
   numbers = [1,2,3,4,5]
   first_number = numbers[0]
   last_number = numbers[-1]
   return first_number, last_number

f, l = simple_function

print(f)
print(l)



