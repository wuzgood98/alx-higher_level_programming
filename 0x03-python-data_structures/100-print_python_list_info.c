#include <Python.h>

/**
 * print_python_list_info - prints the basic info about Python lists.
 * @p: PyObject.
 *
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int idx = 0, size, alloc;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	while (idx < size)
	{
		printf("Element %d: ", idx);

		obj = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		idx++;
	}
}
