# List to iterate
fruits = ['apple', 'banana', 'cherry']

# Using enumerate with default start=0
for index, fruit in enumerate(fruits):
    print(index, fruit)

print()  # Blank line for readability

# Using enumerate with custom start=1
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
