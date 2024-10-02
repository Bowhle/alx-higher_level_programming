#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[.] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;  // Accessing the allocated size
    printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);

        if (strcmp(type, "bytes") == 0) {
            print_python_bytes(item);
        } else if (strcmp(type, "float") == 0) {
            print_python_float(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *bytes = PyBytes_AsString(p);
    printf("[.] bytes object info\n  size: %zd\n  trying string: %.*s\n", size, (int)size, bytes);

    printf("  first %zd bytes: ", size < 10 ? size : 10);
    for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x", (unsigned char)bytes[i]);
        if (i < (size < 10 ? size : 10) - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %f\n", value);
}
