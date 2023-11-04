#include "lists.h"

/**
 * reverse_listint - reverse linked list
 * @head: first node in the list
 * Return: pointer
 */
void reverse_listint(listint_t **head)
{
	listint_t *pre = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = curr->next;
		curr->next = pre;
		pre = curr;
		curr = next;
	}

	*head = pre;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
