#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks if a list is a circle
 * @list: head node
 *
 * Return: 1 on success
 */


int check_cycle(listint_t *list)
{
	listint_t *p, *q;

	q = list;
	p = list;

	while(p && q && q->next)
	{
		p = p->next;
		q = q->next->next;

		if(p == q)
			return(1);
	}

	return(0);
}
