#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints the basic info about Python lists.
 * @p: a PyObject list.
 *
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *object;
	int obj_size, idx = 0, allocated;

	obj_size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", obj_size);
	printf("[*] Allocated = %d\n", allocated);

	while (idx < obj_size)
	{
		printf("Element %d: ", idx);

		object = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(object)->tp_name);

		idx++;
	}
}
