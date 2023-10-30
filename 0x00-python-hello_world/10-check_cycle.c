#include "lists.h"

/**
 * check_cycle - function checks a cycle in list
 * @li: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *li)
{
	listint_t *curr, *ch;

	if (li == NULL || li->next == NULL)
		return (0);
	curr = li;
	ch = curr->next;

	while (curr != NULL && ch->next != NULL
		&& ch->next->next != NULL)
	{
		if (curr == ch)
			return (1);
		curr = curr->next;
		ch = ch->next->next;
	}
	return (0);
}
