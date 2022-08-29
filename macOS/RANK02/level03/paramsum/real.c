#include <unistd.h>

void ft_print(int nb)
{
    if(nb > 9)
        ft_print(nb / 10);
    write(1, &"0123456789"[nb % 10], 1);
}

int main(int ac, char **av)
{
    (void)av;
    if(ac > 1)
        ft_print(ac - 1);
    else
        write(1, "0", 1);
    write(1, "\n", 1);
}