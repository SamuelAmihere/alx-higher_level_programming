#include "lists.h"
#include <stdio.h>

/**
 * list_len - Finds number of elements in a linked
 *
 * @h: struct whose elements to be print elememts
 *
 * Return: number of elements in a linked
 */
size_t list_len(listint_t **h)
{
	size_t count = 0;

	while (*h)
	{
		count += 1;
		*h = (*h)->next;
	}

	return (count);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: A pointer to a singly linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev, *curr;
	int len, i = 0, *temp;

	if (!head || !((*head)->next))
		return (1);

	len = list_len(head);
	temp = malloc(len * sizeof(int));
	if (!temp)
	{
		printf("Could not allocate memory\n");
		exit(1);
	}
	curr = *head;
	prev = NULL;

	/* Move to the end of linkedlist and store the values */
	while (curr)
	{
		temp[i] = curr->n;
		prev = curr;
		curr = curr->next;
		i++;
	}
	free(prev);
	free(curr);
	/* compare the stored values */
	len = 0;
	for (; i >= 0; i--)
	{
		if (temp[i] != temp[len])
		{
			free(temp);
			return (0);
		}
	}
	free(temp);
	return (1);

}
