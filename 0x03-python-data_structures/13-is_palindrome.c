*head = prev;
    return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the pointer of the head node of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half = NULL;
    listint_t *first_half = *head;
    int result = 1; // Assume it is a palindrome

    if (*head == NULL || (*head)->next == NULL)
        return 1; // An empty list or a single node is a palindrome

    // Find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    // Reverse the second half of the list
    second_half = reverse_list(&slow);

    // Compare the first half with the reversed second half
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            result = 0; // Not a palindrome
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the list
    reverse_list(&slow);

    return result;
}
