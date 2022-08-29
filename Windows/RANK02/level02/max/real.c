int		max(int* tab, unsigned int len)
{
    int i = 1;
    int max = tab[0];
    if(!len)
        return(0);
    while(i < len)
    {
        if(tab[i] > max)
            max = tab[i];
        i++;
    }
    return(max);
}

#include <stdio.h>

int	main(void)
{
	int	tab[] = {15, 2, 6, 99, 1};

	printf("%d", max(tab, 5));
	return (0);
}
