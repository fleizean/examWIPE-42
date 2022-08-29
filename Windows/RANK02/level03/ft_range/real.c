#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*tab;
	int	i = 0;

	if (min >= max)
		return (NULL);
	tab = (int *)malloc(sizeof(*tab) * (max - min + 1));
	if (!tab)
        return (NULL);
    while (min <= max)
    {
        tab[i] = min;
        i++;
        min++;
    }
    return (tab);
}

#include <stdio.h>

int	main(void)
{
	int	a;
	int	*tab;

	tab = ft_range(42, 46);
	a = 0;
	while (a < 5)
	{
		printf("%d ", tab[a]);
		a++;
	}
	free(tab);
}