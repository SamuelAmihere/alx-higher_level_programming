#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - Reverses a
 *
 * @head: Starting node
 * @n: size of list
 *
 * Return: 1 on success, -1 on failure
 */
listint_t *reverse_listint(listint_t **head, int *n)
{
	listint_t *temp, *curr;

	if (*head == NULL || (*head)->next == NULL)
		return (*head);

	temp = NULL;
	curr = NULL;
	while (*head)
	{
		curr = (*head)->next;
		(*head)->next = temp;
		temp = *head;
		*head = curr;
		n++;
	}

	*head = temp;

	return (*head);

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
	listint_t *curr, *temp;
	int *n = 0, i = 1;

	if (!head)
		return (1);

	temp = reverse_listint(head, &n);
	curr = *head;

	while (curr && (i * 2 == n || i * 2 -1 == n))
	{
		if (temp->n != curr->n)
			return (0);
		curr = curr->next;
		temp = temp->next;
		i++;
	}
	return (1);

}
