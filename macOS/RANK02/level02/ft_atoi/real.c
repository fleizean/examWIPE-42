int	ft_atoi(const char *str)
{
    int i;
    int rslt;
    int neg;

    i = 0;
    rslt = 0;
    neg = 1;
    while(str[i] <= 32)
        i++;
    if(str[i] == '-')
    {
        neg = -1;
        i++;
    }
    while(str[i] && str[i] >= '0' && str[i] <= '9')
        rslt = (rslt * 10) + (str[i++] - '0');
    return(rslt * neg);
}