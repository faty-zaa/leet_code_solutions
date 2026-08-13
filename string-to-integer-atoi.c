#include <limits.h>

int myAtoi(char *nptr)
{
    int i = 0;
    int s = 1;
    int nj = 0;
    int digit;

    while ((nptr[i] >= 9 && nptr[i] <= 13) || nptr[i] == ' ')
        i++;

    if (nptr[i] == '-' || nptr[i] == '+')
    {
        if (nptr[i] == '-')
            s = -1;
        i++;
    }

    while (nptr[i] >= '0' && nptr[i] <= '9')
    {
        digit = nptr[i] - '0';

        if (nj > INT_MAX / 10 ||
            (nj == INT_MAX / 10 && digit > 7))
        {
            if (s == -1)
                return INT_MIN;
            return INT_MAX;
        }

        nj = nj * 10 + digit;
        i++;
    }

    return nj * s;
}