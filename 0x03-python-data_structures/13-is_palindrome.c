#include "lists.h"
/**
 * reverseList - reverses list
 * @head: pointer to head
 * Return: previous pointer
 */

listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: double pointer to head
 * Return: 0 if not palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *secondHalf;
	listint_t *temp1;
	listint_t *temp2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	secondHalf = reverseList(slow->next);
	temp1 = *head;
	temp2 = secondHalf;

	while (temp2 != NULL)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	reverseList(secondHalf);
	return (1);
}
