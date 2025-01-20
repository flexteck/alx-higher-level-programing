#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - print basic info about a python list
 *
 * p: list that the info is to be printed
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item = NULL;
	const char *type_name;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		allocated = ((PyListObject *)p)->allocated;

		printf("[*] Size of the python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			type_name = Py_TYPE(item)->tp_name;

			printf("Element %zd: %s\n", i, type_name);
		}
	}
	else
	{
		printf("Passed object is not a List\n");
	}
}
