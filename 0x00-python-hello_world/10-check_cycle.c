#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the list
 * @list: linked list to be checked
 *
 * Return: 0 if there is no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_temp, *fast_temp;

	slow_temp = list;
	fast_temp = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast_temp != NULL && fast_temp->next != NULL)
	{
		slow_temp = slow_temp->next;
		fast_temp = fast_temp->next->next;

		if (fast_temp == slow_temp)
			return (1);
	}
	return (0);
}
