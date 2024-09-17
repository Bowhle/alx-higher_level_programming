#include "lists.h"
#include <stdio.h>

/**
 * reverse - Reverses a linked list.
 * @head: Pointer to the pointer of the head of a linked list.
 */
void reverse(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}

/**
 * compare_lists - Compares two lists.
 * @head1: Pointer to the head of the first list.
 * @head2: Pointer to the head of the second list.
 * @len: Length of the lists.
 * Return: 1 if the lists are the same, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2, int len)
{
    for (int i = 0; i < len; i++)
    {
        if (head1 == NULL || head2 == NULL)
            return (0);
        if (head1->n != head2->n)
            return (0);
        head1 = head1->next;
        head2 = head2->next;
    }
    return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to pointer of the first node in listint_t list.
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half;
    listint_t *first_half;
    int len = 0;

    if (head == NULL || *head == NULL)
        return (1);

    // Find the length of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
        len++;
    }

    // Adjust for odd length list
    if (fast != NULL)
        len++;

    first_half = *head;
    second_half = slow;

    // Reverse the second half of the list
    reverse(&second_half);

    // Compare the two halves
    int result = compare_lists(first_half, second_half, len / 2);

    // Restore the list (optional)
    reverse(&second_half);

    return result;
}
