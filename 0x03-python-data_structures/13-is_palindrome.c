#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - Reverses a
 *
 * @head: Starting node
 *
 * Return: 1 on success, -1 on failure
 */
listint_t *reverse_listint(listint_t **head)
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
	listint_t *prev, *curr, *temp = reverse_listint(head);

	if (!head)
		return (1);

	curr = *head;
	prev = NULL;

	while (curr)
	{
		if (temp->n != curr->n)
			return (0);
		prev = curr;
		curr = curr->next;
		temp = temp->next;
	}
	(void)prev;
	return (1);

}
