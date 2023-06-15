#include "lists.h"

/**
* print_dlistint - print elements of the list
* @h: pointer to the head
* Return: number of elemnts in list
*/

size_t print_dlistint(const dlistint_t *h)
{
	int n = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		n++;
	}
	return (n);
}
