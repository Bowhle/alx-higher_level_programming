#define PyObject_Check(obj) ((obj) != NULL && (obj)->ob_type != NULL)

#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);

    const char *str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

    printf("  first %s bytes: ", (size < 10) ? "0" : "10");
    for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i + 1 < (size < 10 ? size : 10)) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}
