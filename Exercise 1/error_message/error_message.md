## Script 1
print("This is a simple test"
print("Oha, it does not work.")
Here I am getting SyntaxError. Because I didn't closed the parentheses for the first print. It should be like this: print("This is a simple test")
SyntaxError: An error in the syntax of a string of characters or tokens meant to be written in a certain programming language is known as a syntax error in computer science. Syntax mistakes in compiled languages are found during compilation. The syntax problems in a programme must all be fixed before it can be built. (source of definition: https://en.wikipedia.org/wiki/Syntax_error)

## Script 2
mass_in_kg = 10
force = mass_in_kg * gravitational_acceleration
print(f"{mass_in_kg} get's accelerated with a force of {force} on earth.")
Here I am getting NameError, Because I am trying to use gravitational_accelaration variable which actually doesn't exist in code. Even if it exist also if I try to use it before it's defined I will get this error. So basically it's not defined before using it.To fix this , we just need to add this variable with a value.For example:
mass_in_kg = 10
gravitational_acceleration = 9.81
force = mass_in_kg * gravitational_acceleration
print(f"{mass_in_kg} get's accelerated with a force of {force} on earth.")
NameError: When a Python programme tries to access or utilise a variable that hasn't been defined or given a value, a NameError: name 'x' is not defined error is thrown. This might take place if the variable's name is misspelt or if it is used before it has been defined. 
(source of definition: https://rollbar.com/blog/undefined-variable-nameerror-python/#:~:text=In%20Python%2C%20a%20NameError%3A%20name,before%20it%20has%20been%20defined.)
## Script 3
from Math import sqrt
a = 9
print(f"The square root of {a} is {sqrt(a)}.")
Here I am getting ModuleNotFoundError. Because I am trying to get a method name sqrt from module named 'Math' , which doesn't exist in python. However there is a module named 'math'. Which has this function exported. Module names are case sensitive. To fix this we need to:
from math import sqrt
a = 9
print(f"The square root of {a} is {sqrt(a)}.")
ModuleNotFoundError: Incorrect spelling of the module name - The Python interpreter will report the ModuleNotFoundError if you have misspelt the module's name, which prevents it from being found.
(source of definition: https://www.javatpoint.com/modulenotfounderror-no-module-named-python#:~:text=Incorrect%20spelling%20of%20the%20module,prevents%20it%20from%20being%20found.&text=The%20module%20is%20not%20installed,import%20it%20into%20your%20code.)
## Script 4
print "Let's run some legacy code..."
Here I am getting SyntaxError. Because in python3 print is a function not a statement. So it should be called with parentheses. But in python 2 it may work. To fix this I have to call like this: 
print("Let's run some legacy code...");
## Script 5
print("Let's repeat this" * 3.)
Here I am getting a TypeError. Which is saying i can't multiply string with non integer. In python, you can multiply string with only integers. But here it's float. To fix this just do like this:
print("Let's repeat this" * 3)
TypeError: TypeError is an exception in Python programming language that occurs when the data type of objects in an operation is inappropriate. For example, If you attempt to divide an integer with a string, the data types of the integer and the string object will not be compatible. Due to this,  the Python interpreter will raise a TypeError exception as shown in the following example.
(source of definition: https://www.pythonforbeginners.com/basics/typeerror-in-python)
## Script 6
age = int(input("Your age: "))
if age < 18:
    print("Sorry, we don't serve minors here")
  else:
    print("What can i serve you?")
Here I am getting IndentationError. In python indentation is very important it creates the scope. For example here if else is a block. So else should be at same indented as it's if block. To fix this:
age = int(input("Your age: "))
if age < 18:
    print("Sorry, we don't serve minors here")
else:
    print("What can i serve you?")
## Script 7
while input("What can I server you? ") != "Gin"
    print("Awful choice, try again.")
print("Good choice.")
Here I am getting SyntaxError. Because in python for while loop the correct syntax is to put a colon after the logic. To fix it:
while input("What can I server you? ") != "Gin":
    print("Awful choice, try again.")
print("Good choice.")