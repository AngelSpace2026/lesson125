#Lessons 1-6
# Prints the raw string 'Hello' without any special character interpretation
print(r'Hello')

# Same as the previous line, prints 'Hello' again
print(r'Hello')

# Prints 'Hello' followed by a newline, so the next output appears on a new line
print('Hello\n')

# Raw string: escape sequences like '\n' are not processed, so it prints as is
print(r'Line 1\nLine 2\nLine 3')

# Same as the previous line, prints the raw string
print(r'Line 1\nLine 2\nLine 3')

# Again, same output as before
print(r'Line 1\nLine 2\nLine 3')

# Prints the string 'print("Hello world")' literally, without executing the inner print
print('print("Hello world")')

# Concatenates the strings and prints 'Hello Jenny'
print("Hello" + " " + "Jenny")

# lesson 7 
print("Hello" + " " + input("What is your name? "))