# Two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

# Using zip to pair elements
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Converting zipped object to a list of tuples
zipped_list = list(zip(names, scores))
print(zipped_list)
