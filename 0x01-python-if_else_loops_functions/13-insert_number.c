#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - A function that insert a number into a sorted
 * node
 *
 * @head: the head node
 * @number: the number to be inserted
 * Return: address of the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));

	if (!new)
		return(NULL);

	new->n = number;
	new->next = NULL;

	current = *head;

	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return(new);
}
