# Python Functions Practice

# Simple function
def greet(name):
    return "Hello, " + name

print(greet("Susmitha"))

# Addition function
def add(a, b):
    return a + b

print("Addition:", add(10, 20))

# Square function
def square(num):
    return num * num

print("Square:", square(5))

# Function with default argument
def to_smash(total_candies, friends=3):
    return total_candies % friends

print("Remaining candies:", to_smash(10))

# Maximum of two numbers
def maximum(a, b):
    return max(a, b)

print("Maximum:", maximum(15, 25))
