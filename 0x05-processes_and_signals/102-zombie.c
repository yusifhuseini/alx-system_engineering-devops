#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 *infinite_while - Creates an infinite loop to keep the program running.
 *
 *Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 *main - Entry point of the program
 *
 *Return: Always returns 0.
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork(); /*Create a child process */

		if (child_pid == -1)
		{
			perror("Error creating child process");
			exit(1);
		}

		if (child_pid == 0)
		{ /*Child process */
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else
		{ /*Parent process */
			sleep(1); /*Sleep for 1 second to allow child to become a zombie */
		}
	}

	infinite_while(); /*Enter an infinite loop to keep the program running */

	return (0);
}
