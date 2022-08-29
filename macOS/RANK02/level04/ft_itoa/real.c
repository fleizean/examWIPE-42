#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int find_strlen(int nb)
{
    int count = 0;
    if(nb > 9)
    {
        find_strlen(nb / 10);
        count++;
    }
    return(count);
}

char	*ft_itoa(int nbr)
{
    int len = 0;
    int neg = 1;
    char *str;
    if (nbr == -2147483648)
        return ("-2147483648");
    len =  find_strlen(nbr);
    if(nbr < 0)
    {
        len += 1;
        nbr *= -1;
        neg = -1;
    }
    if(!(str = (char *)malloc(sizeof(char) * len + 1)))
        return (NULL);
    str[len] = '\0';
    if(neg == -1)
    {
        str[0] = '-';
    }
    while(nbr)
    {
        str[len] = (nbr % 10) + '0';
        nbr /= 10;
        len--;
    }
    return(str);
}

int main()
{
    printf("%s",ft_itoa(0));
}