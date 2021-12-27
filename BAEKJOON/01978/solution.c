#include <stdio.h>
 
int is_prime(int n);
 
int main()
{
    int n;
    int i;
    int count = 0;
    int lim;
 
    scanf("%d", &lim);
 
    for (i = 0; i < lim; ++i)
    {
        scanf("%d", &n);
        if (is_prime(n)) { ++count; }
    }
    
    printf("%d\n", count);
    
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
                if (n%i == 0)
                {
                    return 0;
                }
            }
        }
        else
        {
            return 0;
        }
    }
 
    return 1;
}
