#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints a Python string object.
 * @p: A pointer to the Python object.
 */
void print_python_string(PyObject *p)
{
    // Check if the passed object is a string
    if (!PyUnicode_Check(p))
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get the length and value of the string
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *value = PyUnicode_AsUTF8(p); // Convert to UTF-8 string

    // Check if the conversion was successful
    if (value == NULL)
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Determine the type of string object (ASCII or Unicode)
    const char *type = "compact unicode object"; // Default to unicode
    if (length < 256) // Length for compact ASCII
    {
        type = "compact ascii"; // Compact ASCII
    }

    // Print the string object info
    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);
}
