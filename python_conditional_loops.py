# Python Conditionals and Loops Practice

# Even or Odd
num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Positive or Negative
num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Find the largest of three numbers
a = 10
b = 25
c = 15

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)

# For loop
for i in range(1, 6):
    print(i)

# While loop
count = 1

while count <= 5:
    print(count)
    count += 1

# Multiplication table
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Sum of numbers
total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)
