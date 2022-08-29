#include <unistd.h>

int check(char *str, char c, int nb)
{
    int i = 0;
    while(i < nb)
    {
        if(str[i] == c)
            return(1);
        i++;
    }
    return(0);
}
void inter(char *s1, char *s2)
{
    int i;
    int j;

    i = 0;
    while(s1[i])
    {
        j = 0;
        while(s2[j])
        {
            if(s1[i] == s2[j])
            {
                if(check(s1, s1[i], i) == 1)
                {
                    write(1, &s1[i], 1);
                    break;
                }
            }
            j++;
        }
        i++;
    }
}
int main(int ac, char **av)
{
    if(ac == 3)
        inter(av[1],av[2]);
    write(1, "\n", 1);
}