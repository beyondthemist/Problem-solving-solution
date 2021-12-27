// https://www.acmicpc.net/problem/2581

#include <stdio.h>
 
int is_prime(int n);
 
int main()
{
    int m, n;
    int sum = 0;
    int i;
    int min = -1;
 
    scanf("%d", &m);
    scanf("%d", &n);
 
    for (i = m; i <= n; ++i)
    {
        if (is_prime(i)) 
        { 
            min = i; 
            break;
        }
    }
 
    if(min == -1) { printf("-1\n"); }
    else
    {
        sum += i++;
 
        for (; i <= n; ++i)
        {
            if (is_prime(i)) { sum += i; }
        }
 
        printf("%d\n", sum);
        printf("%d\n", min);
    }
 
    return 0;
}
 
int is_prime(int n)
{
    int i;
 
    if (n != 2)
    {
        if ((n % 2) && (n != 1)) //Odd
        {
            for (i = 3; i*i <= n; i += 2)
            {
                if (n%i == 0) { return 0; }
            }
        }
        else { return 0; }
    }
 
    return 1;
}
