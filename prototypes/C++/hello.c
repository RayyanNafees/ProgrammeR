#include <stdio.h>

int main(void)
{
    char msg[13] = "Hello World!";
    for(int i = 0; i<12; i++)
        printf("%c",msg[i]);
}
