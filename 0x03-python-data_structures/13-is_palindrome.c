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
listint_t *reverse_listint(listint_t **head, size_t *n)
{
	listint_t *temp, *curr;
	size_t count = 0;

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

		count++;
	}

	*head = temp;
	*n = count;

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
	int n = 0, i = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = reverse_listint(head, (size_t *) &n);
	curr = *head;

	while (curr && (i * 2 <= n || i * 2 -1 <= n))
	{
		i++;
		if (temp->n != curr->n)
			return (0);
		curr = curr->next;
		temp = temp->next;
	}
	return (1);

}
