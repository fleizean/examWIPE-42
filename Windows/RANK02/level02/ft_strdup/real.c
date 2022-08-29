#include <stdlib.h>

int ft_strlen(char *str)
{
    int i = 0;
    while(str[i])
        i++;
    return(i);
}

char    *ft_strdup(char *src)
{
    int i = 0;
    int len = ft_strlen(src);
    char *dst = malloc(sizeof(char) * len + 1);

    while(src[i])
    {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';
    return(dst);
}