# Python - Input/Output

Input and output (I/O) refer to the processes of interacting with external data sources, such as reading from and writing to files, receiving user input from the keyboard, and displaying information to the console or other output devices. Python provides several built-in functions and modules to facilitate I/O operations.

![](https://raw.githubusercontent.com/thecoducer/python_programs/master/Images/python-harry-potter.jpg)

## Reading User Input:

The input() function is used to read user input from the keyboard. It reads a line of text entered by the user and returns it as a string.
```user_input = input("Enter something: ")```

## Standard Output (Printing):

The print() function is used to display information to the console or standard output. You can print variables, strings, and any other data you want to display.
```print("Hello, World!")```
## File I/O:

Python allows you to work with files using the open() function to open a file and various methods for reading (read(), readline(), readlines()) and writing (write(), writelines()) data.
```
# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()

# Writing to a file
with open("output.txt", "w") as file:
    file.write("This is some content.")
```
## Standard Input/Output Redirection:

You can redirect standard input and output to and from files or other streams using the < and > operators or by using the sys module's stdin and stdout objects.

```python script.py < input.txt > output.txt```
## Formatted Output:

Python supports string formatting for more complex output, using techniques like f-strings, the format() method, or the % operator.
```
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```
