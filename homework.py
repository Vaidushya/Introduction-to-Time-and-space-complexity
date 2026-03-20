# Functions
def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for i in range(b):
        result += a
    return result


# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling both functions
result1 = multiply_one_iteration(num1, num2)
result2 = multiply_n_iterations(num1, num2)

# Display results
print("Result using 1 iteration:", result1)
print("Result using N iterations:", result2)