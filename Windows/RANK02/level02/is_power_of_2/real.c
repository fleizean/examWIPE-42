int	    is_power_of_2(unsigned int n)
{
    while(n > 1 && n % 2 == 0)
        n /= 2;
    return(n == 1);
}

#include <stdio.h>

int	main(void)
{
	printf("%d", is_power_of_2(7));
}
