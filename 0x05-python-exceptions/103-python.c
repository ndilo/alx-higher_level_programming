#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n  size: %zd\n  trying string: %s\n", size, PyBytes_AsString(p));

    Py_ssize_t max_print = size < 10 ? size : 10;
    printf("  first %zd bytes: ", max_print);
    for (Py_ssize_t i = 0; i < max_print; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %lf\n", value);
}
