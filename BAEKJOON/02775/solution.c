// https://www.acmicpc.net/problem/2775

#include <stdio.h>
 
#define HOUSES 14
#define FLOORS 15
 
int main()
{
    int apart[FLOORS][HOUSES];
    int t, i, j;
    int k, n;
 
    /*initialize*/
    for (i = FLOORS - 1; i >= 0; --i) apart[i][0] = 1;
    for (j = 1; j < HOUSES; ++j) apart[FLOORS - 1][j] = (j + 1);
    for (i = FLOORS -2; i >= 0; --i)
    {
        for (j = 1; j < HOUSES; ++j)
        {
            apart[i][j] = apart[i + 1][j] + apart[i][j - 1];
        }
    }
 
    scanf("%d", &t);
    for (; t > 0; --t)
    {
        scanf("%d", &k);
        scanf("%d", &n);
 
        printf("%d\n", apart[FLOORS - 1 - k][n - 1]);
    }
 
    return 0;
}
