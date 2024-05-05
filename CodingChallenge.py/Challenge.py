# Python Coding Challenges on Numbers 
# Write a program in Python to -

# 1. Convert decimal numbers to octal numbers.
# 2. Reverse an integer.
# 3. Print the Fibonacci series using the recursive method.
# 4. Find the average of numbers (with explanations).
# 5. Convert Celsius to Fahrenheit.


# The solutions of the questions are given below:
# 1. Convert decimal numbers to octal numbers.

# In case you dont know what octal numbers are : Octal numbers are numbers that use a base of 8 and digits 0 - 7

decimal_number = int(input("Enter the decimal number: "))
octal_number = oct(decimal_number)[2:]
print(octal_number)  

# 2. Reverse an integer.

number = int(input("Enter your integer: "))
reversed_no = int(str(number)[::-1])
print(reversed_no)

# 3. Print the Fibonacci series using the recursive method.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# # Printing the Fibonacci series up to the 10th number
x = int(input('Enter the nth number up to which you want the series: '))
for i in range(x):
    print(fibonacci(i))

# 4. Find the average of numbers (with explanations).

def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    else:
        total = sum(numbers)
        average = total / len(numbers)
        return average

number_list = [2, 4, 6, 8, 10]
avg = calculate_average(number_list)
print(avg) 

# 5. Convert Celsius to Fahrenheit.

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")