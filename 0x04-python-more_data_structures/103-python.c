#include <Python.h>
/**
 * print_python_list - prints python lists
 * @p: pyobject
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		PyObject *item;
		Py_ssize_t i;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "Invalid Python List Object\n");
	}
}

/**
 * print_python_bytes - prints python bytes objects
 * @p: pyobject
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t max_print = size > 10 ? 10 : size;

		printf("[.] bytes object info\n");
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));

		printf("  first %zd bytes:", max_print);
		for (Py_ssize_t i = 0; i < max_print; i++)
		{
			printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "Invalid Python Bytes Object\n");
	}
}
