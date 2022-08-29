#include <stdlib.h>
#include <unistd.h>

void ft_putstr(char *str)
{
    int i = 0;
    while(str[i])
    {
        write(1, &str[i], 1);
        i++;
    }
}

char    **ft_split(char *str)
{
    int i;
    int k;
    int j;
    char **split;

    i = 0;
    k = 0;
    if(!(split = (char **)malloc(sizeof(char) * 256)))
        return(NULL);
    while(str[i] <= 32)
        i++;
    while(str[i])
    {
        j = 0;
        if(!(split[k] = (char *)malloc(sizeof(char) * 4096)))
            return(NULL);
        while(str[i] > 32 && str[i])
            split[k][j++] = str[i++];
        while(str[i] <= 32 && str[i])
            i++;
        split[k][j] = '\0';
        k++;
    }
    split[k] = NULL;
    return(split);
}

int main(int ac, char **av)
{
    int i = 1;
    char **str;
    if(ac == 2)
    {
        str = ft_split(av[1]);
        while(str[i])
        {
            ft_putstr(str[i]);
            write(1, " ", 1);
            i++;
        }
        ft_putstr(str[0]);
    }
    write(1, "\n", 1);
}