#include <unistd.h>

void ft_print(int nb)
{
    if(nb > 9)
        ft_print(nb / 10);
    write(1, &"0123456789"[nb % 10], 1);
}

int ft_atoi(char *str)
{
    int i;
    int rslt;

    i = 0;
    rslt = 0;
    while(str[i] && str[i] >= '0' && str[i] <= '9')
        rslt = (rslt * 10) + (str[i++] - '0');
    return(rslt);
}

int main(int ac, char **av)
{
    int s1 = 0, i = 1;
    if(ac == 2)
    {
        s1 = ft_atoi(av[1]);
        while(i <= 9)
        {
            ft_print(i);
            write(1, " x ", 3);
            ft_print(s1);
            write(1, " = ", 3);
            ft_print(s1 * i);
            if(i != 9)
                write(1, "\n", 1);
            i++;
        }
    }
    write(1, "\n", 1);
}