#include <unistd.h>

void expand_str(char *str)
{
    int i = 0;
    while(str[i] <= 32)
        i++;
    while(str[i])
    {
        if(str[i] <= 32)
        {
            if(str[i + 1] > 32 && str[i + 1])
                write(1, "   ", 3);
        }
        else
            write(1, &str[i], 1);
        i++;
    }
}
int main(int ac, char **av)
{
    if(ac == 2)
        expand_str(av[1]);
    write(1, "\n", 1);
}