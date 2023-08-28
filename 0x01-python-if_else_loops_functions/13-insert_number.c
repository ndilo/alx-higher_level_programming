#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: pointer to the list
 * @number: number to add
 * Return: address of the added node else NULL
 *
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old_node, *new_node, *current;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	old_node = NULL;
	current = *head;

	for (; current != NULL && current->n < number;)
	{
		old_node = current;
		current = current->next;
	}

	new_node->next = current;

	if (old_node != NULL)
		old_node->next = new_node;
	else
		*head = new_node;

	return (new_node);
}
