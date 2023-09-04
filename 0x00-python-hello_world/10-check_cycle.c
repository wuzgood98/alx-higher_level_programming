#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly-linked list contains a cycle
 * @list: a singly-linked list.
 *
 * Return: 0 if there is no cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *hard, *headed;

	if (list == NULL || list->next == NULL)
		return (0);

	hard = list->next;
	headed = list->next->next;

	while (hard && headed && headed->next)
	{
		if (hard == headed)
			return (1);
		hard = hard->next;
		headed = headed->next->next;
	}

	return (0);
}
