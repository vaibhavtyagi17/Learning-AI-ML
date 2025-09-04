# Regular function
def outer_function(x):
    print("Outer function called with x =", x)

    # Nested function (inner function)
    def inner_function(y):
        print("Inner function called with y =", y)
        return x + y

    # Call the nested function from outer
    result = inner_function(x + 1)
    print("Result from inner_function:", result)
    return result

# Call the outer function (which itself calls the nested function)
output = outer_function(5)
print("Final output:", output)
def serve():
    chai_type="lemon" #local scope
    print(f"the chai selected is : {chai_type}")

chai_type="masala" #global scope
serve()
print(f"the chai selected is : {chai_type}")

def chai_counter():
    chai_order="lemon" #enclosing scope
    def print_order():
        chai_order="ginger"
        print(f"the chai order is : {chai_order}")
    print_order()
    print(f"the chai order is : {chai_order}")
chai_counter()