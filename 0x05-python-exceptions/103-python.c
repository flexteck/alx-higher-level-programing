#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdio.h>


/**
 * print_python_list - function that print info about a list
 * @p: pointer to the list
 */

void print_python_list(PyObject *p)
{
	PyListObject *List;
	Py_ssize_t size, i;
	PyObject *item;
	Py_ssize_t allocated;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf(" [Error] Invalid List Object\n");
		fflush(stdout);
	}

	List = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	allocated = List->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	fflush(stdout);

	for (i = 0; i < size; i++)
	{
		item = List->ob_item[i];

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		fflush(stdout);
	}
}


/**
 * print_python_bytes - function that prints info about an
 * an object byte
 * @p: pointer to the object
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte;
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	fflush(stdout);

	if (!PyBytes_Check(p))
	{
		printf("[Error] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	byte = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	str = byte->ob_sval;

	printf(" Size: %zd\n", size);
	printf(" Trying String: %s\n", str);

	printf(" first %zd bytes: ", (size < 10) ? size:10);
	fflush(stdout);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx ", str[i]);
	}

	printf("\n");
	fflush(stdout);
	
}


/**
 * print_python_float - function that print info about a float 
 * object.
 *
 * @p: pointer to the float object
 */


void print_python_float(PyObject *p)
{
	double f_value;

	if (!PyFloat_Check(p))
	{
		printf("[.] Python list info\n");
		printf("[Error] Invalid Float Oject\n");
		fflush(stdout);

		return;
	}

	f_value = ((PyFloatObject *)p)->ob_fval;
	printf("[.] float object info\n");
	printf("value: %g\n", f_value);
	fflush(stdout);
}
