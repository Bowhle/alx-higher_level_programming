#include "lists.h"

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
    unsigned int count = 0;

    while (head)
    {
        if (count == index)
            return head;
        head = head->next;
        count++;
    }
    return NULL; // if the node does not exist
}