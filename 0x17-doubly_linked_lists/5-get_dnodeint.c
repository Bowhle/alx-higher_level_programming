#include "lists.h"

/**
 * get_dnodeint_at_index - Returns the nth node of a dlistint_t linked list
 * @head: Pointer to the head of the list
 * @index: The index of the node to return
 *
 * Return: The address of the node at index, or NULL if the node does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int count = 0;

	while (head != NULL)
	{
		if (count == index)
		{
			return (head);  /* Return the node if the index matches */
		}
		head = head->next;  /* Move to the next node */
		count++;            /* Increment the count */
	}

	return (NULL);  /* Return NULL if the node does not exist */
}
