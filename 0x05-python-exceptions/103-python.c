/*
 * File: 103-python.c
 * Auth: OLADAPO ODEDEYI
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    const char *type;

    // Check if the input is a valid list object
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    // Get the size and allocated space
    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        type = Py_TYPE(item)->tp_name; // Get the type name
        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
        else if (strcmp(type, "float") == 0)
            print_python_float(item);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    const char *bytes_str;

    // Check if the input is a valid bytes object
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    fflush(stdout);

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    bytes_str = PyBytes_AsString(p); // Get the string representation

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_str ? bytes_str : "None");

    // Print the first 10 bytes or less if the size is smaller
    size = (size > 10) ? 10 : size;
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", (unsigned char)bytes_str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
    char *buffer = NULL;
    PyFloatObject *float_obj;

    // Check if the input is a valid float object
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    fflush(stdout);

    printf("[.] float object info\n");
    float_obj = (PyFloatObject *)p;
    buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
            Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer);
}
