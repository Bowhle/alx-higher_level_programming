#include "lists.h"

/**
 * check_cycle - function that checks if a linked list has a cycle in it
 *
 * @list: list of parameters
 * Return: 1 if there is no cycle, 0 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *speed, *slow;

	if (!list || !list->next)
		return (0);
	speed = list->next->next;
	slow = list;

	while (slow && speed && speed->next)
	{
		if (slow == speed)
			return (1);
		slow = slow->next;
		speed = speed->next->next;
	}
	return (0);
}
