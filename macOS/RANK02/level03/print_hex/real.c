#include <unistd.h>

void ft_print(int nb)
{
    if(nb > 15)
        ft_print(nb / 16);
    write(1, &"0123456789abcdef"[nb % 16], 1);
}

int ft_atoi(char *str)
{
    int i = 0;
    int rslt = 0;
    while(str[i] && str[i] >= '0' && str[i] <= '9')
        rslt = (rslt * 10) + (str[i++] - '0');
    return(rslt);
}

int main(int ac, char **av)
{
    if(ac == 2)
        ft_print(ft_atoi(av[1]));
    write(1, "\n", 1);
}