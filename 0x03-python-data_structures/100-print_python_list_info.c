#include <object.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about
 * list python objects
 *
 * @p: Python object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int count = 0;
	long int p_size = PyList_Size(p);
	PyListObject *ob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", p_size);
	printf("[*] Allocated = %li\n", ob->allocated);

	while (count < p_size)
	{
		printf("Element %i: %s\n", i,
				Py_TYPE(ob->ob_item[count])->tp_name);
		count++;
	}
}
