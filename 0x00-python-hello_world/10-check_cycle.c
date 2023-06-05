#include "lists.h"

/**
* check_cycle - check if list is cycle
* @list: pointer to header of list
* Return: return 0 if not or 1 if it is
*/

int check_cycle(listint_t *list)
{

	listint_t *n_check;
	listint_t *p_check;

	if (!list)
		return (0);
	p_check = list;
	while (p_check->next)
	{
		n_check = p_check->next;
		while (n_check->next)
		{
			if (n_check == p_check)
				return (1);
			n_check = n_check->next;
		}
		p_check = p_check->next;
	}
	return (0);
}
