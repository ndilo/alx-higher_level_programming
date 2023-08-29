#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item)) {
            printf("bytes\n");
            // Call print_python_bytes(item) here if you want to print bytes info
        } else if (PyFloat_Check(item)) {
            printf("float\n");
            // Call print_python_float(item) here if you want to print float info
        } else if (PyLong_Check(item)) {
            printf("int\n");
            // Handle int objects if needed
        } else if (PyUnicode_Check(item)) {
            printf("str\n");
            // Handle string objects if needed
        } else if (PyTuple_Check(item)) {
            printf("tuple\n");
            // Handle tuple objects if needed
        } else if (PyList_Check(item)) {
            printf("list\n");
            // Handle nested list objects if needed
        } else {
            printf("unknown\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n  size: %ld\n", size);

    char *string = PyBytes_AsString(p);
    printf("  trying string: %s\n", string);

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < 10 && i < size; ++i) {
        printf("%02x ", (unsigned char)string[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %f\n", value);
}
