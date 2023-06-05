#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 *
 * @list: linked list to be checked for cycle
 *
 * Return 1 if cycle exists, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
