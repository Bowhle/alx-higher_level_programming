#include "lists.h"

/**
 * insert_dnodeint_at_index - inserts a new node at a given position
 * @h: double pointer to the head of the list
 * @idx: index of the list where the new node should be added
 * @n: data to insert in the new node
 *
 * Return: the address of the new node, or NULL if it failed or index is out of range
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
    dlistint_t *new_node;
    dlistint_t *current = *h;
    unsigned int count = 0;

    if (idx == 0)
        return (add_dnodeint(h, n)); /* Use existing function to add at head */

    new_node = malloc(sizeof(dlistint_t));
    if (!new_node)
        return (NULL);
    new_node->n = n;

    while (current != NULL && count < idx - 1)
    {
        current = current->next;
        count++;
    }

    if (current == NULL) /* If index is out of range */
    {
        free(new_node);
        return (NULL);
    }

    new_node->next = current->next;
    new_node->prev = current;

    if (current->next != NULL) /* If it's not the last node */
        current->next->prev = new_node;

    current->next = new_node;

    return (new_node);
}
