// https://www.acmicpc.net/problem/1010

#include <stdio.h>
 
int main()
{
    int t, m, n;
    int i, result;
 
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d %d", &n, &m);
        result = 1;
        for (i = 0; i < ((n > m / 2) ? (m - n) : n); i++)
        {
            result /= (i + 1);
            result *= (m - i);
        }
 
        printf("%d\n", result);
    }
    
    return 0;
}
