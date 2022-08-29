#include <stdio.h>

int main(int ac, char **av)
{
    int s1 = 0;
    int s2 = 0;
    int rslt = 0;
    if(ac == 4)
    {
        s1 = atoi(av[1]);
        s2 = atoi(av[3]);
        if(av[2][0] == '+')
            rslt = s1 + s2;
        else if(av[2][0] == '-')
            rslt = s1 - s2;
        else if(av[2][0] == '*')
            rslt = s1 * s2;
        else if(av[2][0] == '/')
            rslt = s1 / s2;
        else if(av[2][0] == '%')
            rslt = s1 % s2;
        printf("%d",rslt);
    }
    write(1, "\n", 1);
}