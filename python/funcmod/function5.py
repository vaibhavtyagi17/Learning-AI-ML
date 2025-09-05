def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Example usage
print(factorial(5))  # Output: 120
chai_types=["masala","ginger","kadak","lemon"]
strong_chai=list(filter(lambda chai:chai!="kadak",chai_types))
print(strong_chai)