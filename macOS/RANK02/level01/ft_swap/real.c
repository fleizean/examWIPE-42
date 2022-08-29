#include <stdio.h>
#include <unistd.h>

void	ft_swap(int *a, int *b)
{
	int	i;

	i = *a;
	*a = *b;
	*b = i;
}

int	main(void)
{
	int	x = 3;
	int	y = 5;
	int	*p = &x;
	int	*r = &y;
	ft_swap(p, r);
	printf("%d", *p);
	printf("%d", *r);
}
