#include "lists.h"
/**
 * check_cycle - checks if linked list is cyclic by using two pointers
 * @list: list to check if cyclic
 * Return: 0 if non-cyclic, 1 if cyclic
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
