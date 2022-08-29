#include <stdlib.h>

int		*ft_rrange(int start, int end)
{
	int		*tab;
	int		i = 0;

	if (start > end)
		tab = (int *)malloc(sizeof(int) * (start - end) + 1);
	else
		tab = (int *)malloc(sizeof(int) * (end - start) + 1);
    while (end > start)
    {
        tab[i] = end;
        end--;
        i++;
    }
    tab[i] = end;
    while (end < start)
    {
        tab[i] = end;
        end++;
        i++;
    }
    tab[i] = end;
    return (tab);
}

#include <stdio.h>

int    main(void)
{
    int    a;
    int    *tab;

    tab = ft_rrange(3, 1);
    a = 0;
    while (a < 5)
    {
        printf("%d ", tab[a]);
        a++;
    }
}
