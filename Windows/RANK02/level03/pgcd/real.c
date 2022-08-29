#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
    int s1 = 0, s2 = 0; 
    if(ac == 3)
    {
        s1 = atoi(av[1]);
        s2 = atoi(av[2]);
        if(s1 > 0 && s2 > 0)
        {
            while(s1 != s2)
            {
                if(s1 > s2)
                    s1 -= s2;
                else
                    s2 -= s1;
            }
            printf("%d",s1);
        }
    }
    printf("\n");
}