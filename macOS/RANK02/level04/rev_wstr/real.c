#include <unistd.h>
#include <stdlib.h>

void	ft_putstr(char *str)
{
	int i;

	i = 0;
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
}

char        **ft_split(char *str)
{
    int i;
    int k;
    int j;
    char **split;

    i = 0;
    k = 0;
    if (!(split = (char **)malloc(sizeof(char *) * 256)))
        return(NULL);
    while (str[i] <= 32)
        i++;
    while(str[i])
    {
        j = 0;
        if (!(split[k] = (char *)malloc(sizeof(char) * 4096)))
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

int		main(int ac, char **av)
{
	int i;
	char **tab;

	i = 0;
	if (ac == 2)
	{
		tab = ft_split(av[1]);
		while (tab[i] != 0)
			i++;
		i--;
		while (i >= 0)
		{
			ft_putstr(tab[i]);
			if (i > 0)
				write(1, " ", 1);
			i--;
		}
	}
	write(1, "\n", 1);
}
