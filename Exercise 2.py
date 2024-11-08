# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 0
x +=3 
print(x)

# TODO: Multiply y by 2 using the *= operator

y = 2
y *= 2
print(y)

# TODO: Divide x by y and store the result in a variable called 'result'

x = 3
y = 10
results = y/x

# TODO: Print the value of 'result'

print(results)

# ------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

a = 2
b = 4
c = 6

# TODO: Create a condition that checks if a is greater than b
# a > b

print(a > b ) 
if a > b :
    print("a is greater than b")
else:
    print("a is less than b")

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)

modulus = b % 2

print(modulus)



# TODO: Create a condition that checks if c is less than or equal to a

# a <= c
# print(a <= c)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

# if a > b :
#     print("a is greater than b")
# elif b%2 :
#     print("b is even")
# elif c <= a: 
#    print("c is less than or equal to a")
# else:
#     print("a is less than c")

final_condition = (a > b ) or (modulus and c <= a)

# TODO: Print the value of 'final_condition'


print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'

while True:
    score_input = input("Enter your test score: ")
    if score_input.isdigit():
        test_score = int(score_input)
        break
    else: 
        print("Please enter a valid test store( numbers only).")

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F

if  test_score >= 90 :
    print("Execllent Job. Grade: A")
elif test_score >= 80 and test_score < 90:
    print("Well done. Grade: B")
elif test_score >=  70: 
    print("Good Job. Grade: C")
elif test_score >= 60: 
    print("Well done. Grade: D")
else:
    print("Do better. Grade: F ")

grade =
if  test_score >= 90 :
    print("Execllent Job. Grade: A")
elif test_score >= 80 and test_score < 90:
    print("Well done. Grade: B")
elif test_score >=  70: 
    print("Good Job. Grade: C")
elif test_score >= 60: 
    print("Well done. Grade: D")
else:
    print("Do better. Grade: F ")



# TODO: Print the grade for the given score

print(f"Your test score : {test_score}" )
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

  
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'

operation = input("Insert operation (+, -, *, /):  ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)

# TODO: Handle the case of division by zero
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(num1 / num2)
else:
    print("Invalid operation")


# TODO: Print the result of the operation
 