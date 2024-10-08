#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it.
 * @list: pointer to the head of the list.
 * 
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (!list || !list->next)
        return (0);

    slow = list;
    fast = list->next;

    while (fast && fast->next)
    {
        if (slow == fast)
            return (1);

        slow = slow->next;
        fast = fast->next->next;
    }

    return (0);
}
