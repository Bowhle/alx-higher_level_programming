#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes the node at a specific index
 * @head: Double pointer to the head of the list
 * @index: The index of the node that should be deleted
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current = *head;
	unsigned int i;

	/* If the list is empty */
	if (current == NULL)
		return (-1);

	/* Deleting the head node */
	if (index == 0)
	{
		*head = current->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(current);
		return (1);
	}

	/* Traverse to the desired index */
	for (i = 0; i < index && current != NULL; i++)
		current = current->next;

	/* If current is NULL, the index is out of bounds */
	if (current == NULL)
		return (-1);

	/* Adjust pointers to remove the node */
	if (current->prev != NULL)
		current->prev->next = current->next;
	if (current->next != NULL)
		current->next->prev = current->prev;

	free(current);
	return (1);
}
