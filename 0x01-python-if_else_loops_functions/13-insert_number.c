#include "lists.h"

/**
 * insert_node - inserts node at a given index
 * @head: pointer to a pointer of the head of the node
 * @number: number to insert.
 *
 * Return: NULL if the operation fails, otherwise a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp_node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (temp_node == NULL || temp_node->n >= number)
	{
		new_node->next = temp_node;
		*head = new_node;
		return (new_node);
	}

	while (temp_node && temp_node->next && temp_node->next->n < number)
	{
		temp_node = temp_node->next;
	}
	new_node->next = temp_node->next;
	temp_node->next = new_node;

	return (new_node);
}
