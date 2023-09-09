#include "lists.h"

int is_palindrome(listint_t **head);
listint_t *reverse_list(listint_t **head);

/**
 * reverse_list - reverses a singly-linked list of type listint_t.
 * @head: a pointer to the node of the list.
 *
 * Return: pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *next, *prev = NULL, *node = *head;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - checks if a single=y-linked list is a palindrome.
 * @head: a pointer to the head of the linked-list of type listint_t.
 *
 * Return: 0 if the linked-list is not a palindrome, otherwise 1.
 */
int is_palindrome(listint_t **head)
{
	size_t list_size = 0, idx;
	listint_t *reverse, *temp, *middle;

	if ((*head)->next == NULL || *head == NULL)
		return (1);

	temp = *head;

	while (temp)
	{
		list_size++;
		temp = temp->next;
	}

	temp = *head;
	for (idx = 0; idx < (list_size / 2) -  1; idx++)
		temp = temp->next;

	if ((list_size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reverse = reverse_list(&temp);
	middle = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}

	reverse_list(&middle);

	return (1);
}
