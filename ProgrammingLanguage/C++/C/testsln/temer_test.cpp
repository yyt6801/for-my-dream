#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/*
    Implementation simple timeout

    Input: count milliseconds as number

    Usage:
        setTimeout(1000) - timeout on 1 second
        setTimeout(10100) - timeout on 10 seconds and 100 milliseconds
 */
void setTimeout(int milliseconds)
{
    // If milliseconds is less or equal to 0
    // will be simple return from function without throw error
    if (milliseconds <= 0)
    {
        fprintf(stderr, "Count milliseconds for timeout is less or equal to 0\n");
        return;
    }

    // a current time of milliseconds
    int milliseconds_since = clock() * 1000 / CLOCKS_PER_SEC;

    // needed count milliseconds of return from this timeout
    int end = milliseconds_since + milliseconds;

    // wait while until needed time comes
    do
    {
        milliseconds_since = clock() * 1000 / CLOCKS_PER_SEC;
    } while (milliseconds_since <= end);
}

int main()
{

    // input from user for time of delay in seconds
    int delay;
    printf("Enter delay: ");
    scanf("%d", &delay);

    // counter downtime for run a rocket while the delay with more 0
    do
    {
        // erase the previous line and display remain of the delay
        printf("\033[ATime left for run rocket: %d\n", delay);

        // a timeout for display
        setTimeout(1000);

        // decrease the delay to 1
        delay--;

    } while (delay >= 0);

    // a string for display rocket
    char rocket[4] = "-->";

    // a string for display all trace of the rocket and the rocket itself
    char *rocket_trace = (char *)malloc(100 * sizeof(char));

    // display trace of the rocket from a start to the end
    int i;
    char passed_way[100] = "";
    for (i = 0; i <= 50; i++)
    {
        setTimeout(25);
        sprintf(rocket_trace, "%s%s", passed_way, rocket);
        passed_way[i] = ' ';
        printf("\033[A");
        printf("| %s\n", rocket_trace);
    }

    // erase a line and write a new line
    printf("\033[A");
    printf("\033[2K");
    puts("Good luck!");

    return 0;
}