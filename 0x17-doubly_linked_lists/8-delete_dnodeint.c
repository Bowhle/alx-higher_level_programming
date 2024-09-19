#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes the node at index index of a dlistint_t linked list
 * @head: double pointer to the head of the list
 * @index: index of the node that should be deleted
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current = *head;
    unsigned int count = 0;

    if (!head || !*head)
        return (-1);

    while (current && count < index)
    {
        current = current->next;
        count++;
    }

    if (!current) // If index is out of range
        return (-1);

    if (current->prev) // If it's not the first node
        current->prev->next = current->next;
    else // If it's the first node
        *head = current->next;

    if (current->next) // If it's not the last node
        current->next->prev = current->prev;

    free(current);
    return (1);
}