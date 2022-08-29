#include <unistd.h>

void	print_bits(unsigned char octet)
{
    int i = 0;
    char bit[7];
    char tmp;
    while(i < 8)
    {
        bit[i++] = octet % 2;
        octet /= 2;
    }
    i--;
    while(i >= 0)
    {
        tmp = bit[i--] + '0';
        write(1, &tmp, 1);
    }
}