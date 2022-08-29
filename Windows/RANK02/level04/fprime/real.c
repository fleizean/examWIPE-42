#include <stdio.h>
#include <stdlib.h>

void fprime(int nb)
{
    int i = 2;
    if(nb <= 1)
        printf("%d", nb);
    while(nb > 1)
    {
        while(nb % i == 0)
        {
            printf("%d",i);
            nb = nb / i;
            if(nb > 1)
                printf("*");
        }
        i++;
    }

}
int main(int ac, char **av)
{
    if(ac == 2)
        fprime(atoi(av[1]));
    printf("\n");
}