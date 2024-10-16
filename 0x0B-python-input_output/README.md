## 0x0B-python-input_output

This README file serves as a reference guide to the common file handling tasks in Python, as well as working with JSON data.

## 2. How to Open a File
In Python, the `open()` function is used to open a file. You need to specify the file name and the mode for opening it.

Example:
```python
file = open("example.txt", "r")  # 'r' stands for read mode 
```

## 3. How to Write Text in a File
To write to a file, you can open it in write mode ("w") and use the write() method.

Example:
```python
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()
```

## 4. How to Read the Full Content of a File
The read() method reads the entire content of a file at once.

Example:
```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

## 5. How to Read a File Line by Line
To read a file line by line, especially useful for large files, use a for loop.

Example:
```python
file = open("example.txt", "r")
for line in file:
    print(line, end="")
file.close()
```

## 6. How to Move the Cursor in a File
Use the seek() method to move the cursor to a specific byte position in the file.

Example:
```python
file = open("example.txt", "r")
file.seek(10)  # Moves cursor to the 10th byte
content = file.read()
print(content)
file.close()
```

## 7. How to Make Sure a File is Closed After Using It
To ensure a file is always closed after you're done with it, use the with statement. This automatically closes the file once the block of code is done executing.

Example:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content) # No need to explicitly close the file
```

## 8. What is and How to Use the with Statement
The with statement is a context manager that ensures proper closure of files.

Example:
```python
with open("example.txt", "r") as file:
```

## 9. What is JSON
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.