# Python Lists and Tuples Practice

# Creating a list
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding elements
numbers.append(60)
print("After append:", numbers)

# Removing elements
numbers.remove(20)
print("After remove:", numbers)

# Sorting
numbers.sort()
print("Sorted list:", numbers)

# List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# Tuple
fruits = ("Apple", "Banana", "Mango")
print("Tuple:", fruits)

# Accessing tuple
print("First fruit:", fruits[0])

# Tuple length
print("Length:", len(fruits))

# Sum and maximum
values = [5, 10, 15, 20]
print("Sum:", sum(values))
print("Maximum:", max(values))
print("Minimum:", min(values))
