#include "lists.h"

/**
 * insert_dnodeint_at_index - Inserts a new node at a given position
 * @h: Double pointer to the head of the list
 * @idx: The index where the new node should be added
 * @n: The data to be added in the new node
 *
 * Return: The address of the new node, or NULL if it failed
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node, *current = *h;
	unsigned int i;

	/* Create a new node */
	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;

	/* Insert at the beginning */
	if (idx == 0)
	{
		new_node->next = current;
		new_node->prev = NULL;
		if (current != NULL)
			current->prev = new_node;
		*h = new_node;
		return (new_node);
	}

	/* Traverse to the desired index */
	for (i = 0; i < idx - 1 && current != NULL; i++)
		current = current->next;

	/* Check if the current is NULL (index out of bounds) */
	if (current == NULL)
	{
		free(new_node);
		return (NULL);
	}

	/* Insert at the specified index */
	new_node->next = current->next;
	new_node->prev = current;

	if (current->next != NULL)
		current->next->prev = new_node;
	current->next = new_node;

	return (new_node);
}
