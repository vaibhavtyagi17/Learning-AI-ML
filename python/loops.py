# for loop over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# for loop with range
for i in range(3):
    print("Number:", i)

# while loop example
number = 0
while number < 3:
    print("While number:", number)
    number += 1

# using break in loops
for i in range(5):
    if i == 3:
        break
    print("Break at", i)

# using continue in loops
for i in range(5):
    if i % 2 == 0:
        continue
    print("Continue at", i)

# for loop with else
for i in range(3):
    print("Looping:", i)
else:
    print("For loop completed.")

# while loop with else
count = 0
while count < 2:
    print("While counting:", count)
    count += 1
else:
    print("While loop completed.")
