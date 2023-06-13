#include "lists.h"

/**
 * is_palindrome - check if a list is palindrom or not
 * @head: address head of list
 * Return: 1 if palindrom or 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	listint_t *rev_list;
	listint_t *tmp_rev;

	tmp = *head;
	if (tmp == NULL || tmp->next == NULL)
		return (1);
	rev_list = reverse_list(tmp);
	tmp_rev = rev_list;
	tmp = *head;
	while (tmp)
	{
		if (tmp->n != rev_list->n)
		{
			free_listint(tmp_rev);
			return (0);
		}
		tmp = tmp->next;
		rev_list = rev_list->next;
	}
	free_listint(tmp_rev);
	return (1);
}

/**
* reverse_list - reverse list
* @list: list base to be reversed
* Return: return new list reversed
*/

listint_t *reverse_list(listint_t *list)
{
	listint_t *new_list;
	listint_t *tmp;
	listint_t *prev = NULL;

	tmp = list;
	while (tmp)
	{
		new_list = malloc(sizeof(listint_t));
		new_list->next = prev;
		new_list->n = tmp->n;
		prev = new_list;
		tmp = tmp->next;
	}
	return (new_list);
}
