// https://www.acmicpc.net/problem/1010

#include <stdio.h>
 
int main()
{
    int t, m, n;
    int lim, i, result;
 
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d %d", &n, &m);
        lim = ((n > m / 2) ? (m - n) : n);
        result = 1;
 
        for (i = 0; i < lim; i++)
        {
            result /= (i + 1);
            result *= (m - i);
        }
 
        printf("%d\n", result);
    }
    
    return 0;
}
