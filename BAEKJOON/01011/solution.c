// https://www.acmicpc.net/problem/1011

#include <stdio.h>
 
#define SQUARE(X) ((X)*(X))
 
int run();
long long warp(long long d);
 
int main()
{
    return run();
}
 
int run()
{
    int num;
    long long x, y;
 
    scanf("%d", &num);
 
    while (--num)
    {
        scanf("%lld %lld", &x, &y);
 
        printf("%lld\n", warp(y - x));
    }
 
    return 0;
}
 
long long warp(long long d)
{
    long long j;
    long long min, sqr, max;
    for (j = 1; ; ++j)
    {
        sqr = SQUARE(j);
        min = sqr - (j - 1);
        max = sqr + j;
        
        if ((min <= d) && (d <= sqr))
        {
            return ((j << 1) - 1);
        }
        else if ((sqr < d) && (d <= max))
        {
            return (j << 1);
        }    
    }
}
