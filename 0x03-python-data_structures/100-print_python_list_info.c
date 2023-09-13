#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints the basic info about Python lists.
 * @p: PyObject.
 *
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *object;
	long int obj_size, idx = 0;
	PyListObject *list;

	obj_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", obj_size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	while (idx < obj_size)
	{
		object = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(object)->tp_name);

		idx++;
	}
}
