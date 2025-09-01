# Integer examples
a = 10
b = -5
c = 0

# Arithmetic operators on integers
print(a + b)  # 5
print(a * b)  # -50
print(a // 3) # Floor division: 3
print(a % 3)  # Modulus: 1
print(a ** 2) # Power: 100

# Bitwise operators
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 2) # Left shift (multiply by 4)
print(a >> 1) # Right shift (divide by 2)
# Float examples
x = 3.14
y = -0.5e2  # -50.0

# Arithmetic operations on floats
print(x + y)   # -46.86
print(x * 2)   # 6.28
print(x / 2)   # 1.57
print(x ** 2)  # 9.8596

# Note: Floor division truncates down to int result when applied to floats
print(y // 4)  # -13.0
# Complex number examples
z1 = 2 + 3j
z2 = 1 - 1j

# Arithmetic on complex numbers
print(z1 + z2)  # (3+2j)
print(z1 * z2)  # (5+1j)
print(z1.real)  # Real part: 2.0
print(z1.imag)  # Imaginary part: 3.0
# Boolean examples
t = True
f = False

# Boolean values as integers
print(int(t))  # 1
print(int(f))  # 0

# Logical operators
print(t and f) # False
print(t or f)  # True
print(not t)   # False

# Mixing booleans with integers
print(t + 5)   # 6
print(f * 10)  # 0
a = 7
b = 3

# Arithmetic
print(a + b)  # Addition: 10
print(a - b)  # Subtraction: 4
print(a * b)  # Multiplication: 21
print(a / b)  # Division: 2.3333333333333335
print(a // b) # Floor division: 2
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 343

# Bitwise (on integers)
print(a & b)  # Bitwise AND: 3
print(a | b)  # Bitwise OR: 7
print(a ^ b)  # Bitwise XOR: 4
print(~a)     # Bitwise NOT: -8
print(a << 1) # Left shift: 14
print(a >> 1) # Right shift: 3
