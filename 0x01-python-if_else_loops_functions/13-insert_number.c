#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
* insert_node - insert node in sorted way
* @head: pointer to header of nodes
* @number: value to be add
* Return: return pointer to new_node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *prev_node;
	listint_t *first_node = *head;

	while (*head)
	{
		if (number < (*head)->n)
		{
			new_node = malloc(sizeof(listint_t));
			if (!new_node)
				return (NULL);
			new_node->n = number;
			new_node->next = *head;
			if (first_node == *head)
			{
				*head = new_node;
				return (new_node);
			}
			prev_node->next = new_node;
			*head = first_node;
			return (new_node);
		}
		prev_node = *head;
		*head = (*head)->next;
	}
	*head = first_node;

	return (add_nodeint_end(&*head, number));
}
