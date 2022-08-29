#include <unistd.h>

void str_capitalizer(char *str)
{
    int i = 0;
    if(str[i] >= 'a' && str[i] <= 'z')
        str[i] -= 32;
    write(1, &str[i], 1);
    i++;
    while(str[i])
    {
        if(str[i] >= 'A' && 'Z' >= str[i])
            str[i] += 32;
        if((str[i] >= 'a' && 'z' >= str[i]) && (str[i - 1] <= 32))
            str[i] -= 32;
        write(1, &str[i], 1);
        i++;
    }
}

#include <stdio.h>
int main(int ac, char **av)
{
    int i = 1;
    if(ac < 2)
        write(1, "\n", 1);
    else
    {
        while(i < ac)
        {
            str_capitalizer(av[i]);
            write(1, "\n", 1);
            i++;
        }
    }
}