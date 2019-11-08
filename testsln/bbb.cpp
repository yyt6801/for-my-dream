#include <stdio.h>
#include "../test_ex_headfile/aaa.h"
int main()
{
    int a = 5;
    int b = 10;
    int c = add(a, b);
    printf("c is %d \n", c);
}