# Using walrus operator in an if statement
if (n := len([1, 2, 3, 4])) > 3:
    print(f"List is too long ({n} elements)")

# Using walrus operator with while loop
numbers = [1, 2, 3, 4, 5]
index = 0
while (num := numbers[index]) < 4:
    print(num)
    index += 1

# Using walrus operator inside a for loop with condition
data = [1, 5, 10, 15]
squares = []
for x in data:
    if (square := x**2) > 50:
        squares.append(square)
print(squares)
