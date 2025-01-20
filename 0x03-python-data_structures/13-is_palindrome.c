#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/* Function to reverse a linked list */
listint_t *rev_link_list(listint_t *head)
{
    listint_t *current = head;
    listint_t *nextnode = NULL;
    listint_t *temp = NULL;

    if (head == NULL)
        return (NULL);
    if (head->next == NULL)
        return (head);

    while (current != NULL)
    {
        nextnode = current->next;
        current->next = temp;
        temp = current;
        current = nextnode;
    }

    return temp;
}

/* Function to compare two linked lists */
int list_compare(listint_t *first, listint_t *second)
{
    while (second)
    {
        if (first->n != second->n)
            return 0;
        first = first->next;
        second = second->next;
    }
    return 1;
}

/* Main function to check if the list is a palindrome */
int is_palindrome(listint_t **head)
{
    listint_t *p = *head;
    listint_t *q = *head;
    listint_t *second_list;

    int flag;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    /* Find the middle of the list */
    while (p != NULL && p->next != NULL)
    {
        p = p->next->next;
        q = q->next;
    }

    /* If p is not NULL, the list has an odd number of elements */
    if (p != NULL)
        q = q->next;

    /* Reverse the second half of the list */
    second_list = rev_link_list(q);

    /* Compare the first half and the reversed second half */
    flag = list_compare(*head, second_list);

    /* Optionally restore the original structure of the list */
    rev_link_list(second_list);

    return flag;
}

