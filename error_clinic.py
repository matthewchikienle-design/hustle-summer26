#Snippet 1 
#Error Prediciton: Will probably not work because anything divided by 0 is "undefined" I believe index error
x = 10
y = 2
result = x/y
print("Result:", result)

#Snippet 2
#Error Prediction: Looking at the code I believe its gonna show an index error because that specific index doesn't exist in the set given, so index
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i - 1])
#Snippet 3
#Error Prediction: Will not run because there is no ":" after the def line syntax
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))
#Snippet 4 
#Error Prediction: Will not run because it's missing ":" Syntax
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    print(is_even(4)) 
    print(is_even(7))
#Snippet 5
#Error Prediction it's missing ":"so Syntax Error
for i in range (5):
    print(i)
#Snippet 6
#Error Prediction: "name" is not joined with "hello" so the code will not work and is a Syntax
def greet(name):
    return ("Hello", name)

print(greet("Alice"))
#Snippet 7 
# Error Prediction: This will be an indentation Error because of an indented block
numbers = [1, 2, 3, 4, 5]
total = 0 
for number in numbers:total += number
print("Sum of numbers:", total)
#Snippet 8
# Error Prediction: It's gonna be a recursion error becauase n + 1 which will continue and not be stopped
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
#Snippet 9
#Error Prediction:No error just works but thinks everyone is greetable
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
        print("Hello," + name)
else:
        print("Hello stanger!")
#Snippet 10
#Error prediction: Won't work because of division by 0, ZeroDivisionError and also Name Error because num and num 2
def divide_numbers(x, y):
     result = x / y 
     return result
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))