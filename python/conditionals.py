# if, elif, else example

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Ternary operator (conditional expression)
y = 20
result = "y is even" if y % 2 == 0 else "y is odd"
print(result)

# match-case statement example (Python 3.10+)
command = "start"

match command:
    case "start":
        print("Starting the process")
    case "stop":
        print("Stopping the process")
    case "pause":
        print("Pausing the process")
    case _:
        print("Unknown command")
