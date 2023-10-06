#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic
 * 	info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int jey;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (jey = 0; jey < Py_SIZE(p); jey++)
		printf("Element %d: %s\n", jey, Py_TYPE(PyList_GetItem(p, jey))->tp_name);
}
