#include <unistd.h>

void ft_print(int nb)
{
    if(nb > 9)
        ft_print(nb / 10);
    write(1, &"0123456789"[nb % 10], 1);
}

int ft_atoi(char *str)
{
    int i = 0;
    int rslt = 0;
    while(str[i] && str[i] >= '0' && str[i] <= '9')
        rslt = (rslt * 10) + (str[i++] - '0');
    return(rslt);
}

int isprime(int nb)
{
    int i = 2;

    while (i < nb)
    {
        if (nb % i == 0)
            return (0);
        i++;
    }
    return (1);
}

void add_prime_sum(int nb)
{
    int i;
    int rslt = 0;
    i = 2;
    if(nb <= 0)
        write(1, "0", 1);
    while(i <= nb)
    {
        if(isprime(i))
            rslt += i;
        i++;
    }
    ft_print(rslt);
}

int main(int ac, char **av)
{
    if(ac == 2)
        add_prime_sum(ft_atoi(av[1]));
    else
        write(1, "0", 1);
    write(1, "\n", 1);
}