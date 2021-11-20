#include "lists.h"
#include <stdio.h>

/**
 * add_nodeaddr - function to add an address node
 *
 * @head: head of list to be added to
 * @address: address to add to list
 *
 * Return: pointer to head node
 */

list_addr *add_nodeaddr(list_addr *head, listint_t *address)
{
	list_addr *head_copy = head;
	list_addr *new_node;

	new_node = malloc(sizeof(list_addr) + sizeof(listint_t));
	new_node->address = address;
	new_node->next = NULL;
	while (head_copy->next != NULL)
		head_copy = head_copy->next;
	head_copy->next = new_node;
	return (head);
}

/**
 * free_addr - function to free linst_addr
 *
 * @head: poiter to head node of list
 *
 * Return: nothing
 */
void free_addr(list_addr *head)
{
	list_addr *current;

	while(head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * check_cycle - function to check if a linked list is a cycle
 *
 * @list: head node of function to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *list_copy = list;
	list_addr *new, *new_copy;

	new = malloc(sizeof(list_addr) + sizeof(listint_t));
	new->address = list_copy;
	new->next = NULL;
	while (list_copy != NULL)
	{
		new_copy = new;
		while (new_copy != NULL)
		{
			if(new_copy->address == list_copy->next)
			{
				free_addr(new);
				return (1);
			}
			new_copy = new_copy->next;
		}
		list_copy = list_copy->next;
		new = add_nodeaddr(new, list_copy);
	}
	free_addr(new);
	return (0);
}
