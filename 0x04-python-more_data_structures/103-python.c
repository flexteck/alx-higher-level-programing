#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_list - print basic info about python lists
 * @P: pyObject pointer (assumed to be python list)
 */

void print_python_list(PyObject *p)
{
	PyListObject *List;
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[Error] Invalid List Object\n");
		return;
	}

	List = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;


	printf("[*] Python list info\n");
    	printf("[*] Size of the Python List = %zd\n", size);
    	printf("[*] Allocated = %zd\n", List->allocated);

	for (i = 0; i < size; i++)
	{
		item = List->ob_item[i];
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}


/**
 * print_python_bytes - print info about python bytes
 * @p: pointer to the python object
 */


void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	str = bytes->ob_sval;

	printf(" size : %zd\n", size);
	printf(" Trying String: %s\n", str);

	printf(" first %zd bytes: ", (size < 10) ? size:10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx ", str[i]);
	}

	printf("\n");
}
