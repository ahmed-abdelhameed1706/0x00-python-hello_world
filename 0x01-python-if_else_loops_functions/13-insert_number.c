#include "lists.h"

/**
 * insert_node - inserts a node in sorted list
 * @head: pointer to head
 * @number: value of data
 *
 * Return: adress of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *temp, *new_node;
	
	prev = NULL;
	temp = *head;

	new_node = malloc(sizeof(listint_t));
	
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		(*head)->next = NULL;
	}
	if (number < (*head)->n)
		new_node->next = *head;

	while (temp != NULL)
	{
		if (number >= temp->n)
		{
			if (temp->next != NULL)
			{
				prev = temp;
				temp = temp->next;
			}
			else
			{
				temp->next = new_node;
				new_node->next = NULL;
			}
		}
		else
		{
			prev->next = new_node;
			new_node->next = temp;
			break;
		}
	}
	return (new_node);
}
