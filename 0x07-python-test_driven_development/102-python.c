#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    // Check if p is a valid Python string object
    if (!PyUnicode_Check(p))
    {
        printf("Error: Invalid String Object\n");
        return;
    }

    // Determine the string type (ASCII or Unicode)
    Py_ssize_t length;
    const char *string_representation = PyUnicode_AsUTF8AndSize(p, &length);

    if (string_representation == NULL)
    {
        printf("Error: Could not convert string to UTF-8\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "unicode object");
    printf("  length: %zd\n", length);
    printf("  value: %s\n", string_representation);
}

