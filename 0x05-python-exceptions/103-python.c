#include <Python.h>
#include <floatobject.h>
#include <stdio.h>
#include <stdlib.h>
#include "/usr/include/python3.4/Python.h"


void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        // You can add more specific information for different types if needed
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *bytes;

    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes:");

    for (i = 0; i < 10 && i < size; i++) {
        printf(" %02x", bytes[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    double value;

    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %f\n", value);
}
