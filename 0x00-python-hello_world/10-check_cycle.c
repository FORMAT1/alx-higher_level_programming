#include "lists.h"

/**
 * check _cycle - checks if a linked list contains a cycle
 * lists: linked lists to check
 *
 * Return: 1 if the list has a cycle, 0 if it dosen't
 */
int check_cycle(listint_t *list)
{
	listint_t *show = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
