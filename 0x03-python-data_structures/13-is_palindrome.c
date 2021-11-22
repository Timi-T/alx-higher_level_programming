#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse - function to reverse a linked list
 *
 * @head: head node of linked list
 *
 * Return: pointer to head of reversed list
 */

listint_t *reverse(listint_t *head)
{
	listint_t *prev, *current, *next_node;

	if (head->next == NULL)
		return (head);
	current = head;
	next_node = current->next;
	current->next = NULL;
	while (next_node->next != NULL)
	{
		prev = current;
		current = next_node;
		next_node = next_node->next;
		current->next = prev;
	}
	next_node->next = current;
	return (next_node);
}

/**
 * is_palindrome - function to check if a linked list a palindrome
 *
 * @head: pointer to head node of linked list
 *
 * Return: 0 if its not and 1 if its a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *rev_copy;
	listint_t **head_copy = head;
	listint_t *head_copy2 = *head;
	int i = 0;

	rev = NULL;
	while (*head_copy != NULL)
	{
		add_nodeint_end(&rev, (*head_copy)->n);
		*head_copy = (*head_copy)->next;
	}
	rev = reverse(rev);
	rev_copy = rev;
	while (rev_copy != NULL)
	{
		if (rev_copy->n != (head_copy2)->n)
			return (0);
		rev_copy = rev_copy->next;
		head_copy2 = (head_copy2)->next;
		i++;
	}
	return (1);
}
