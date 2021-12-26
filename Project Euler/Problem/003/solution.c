// https://euler.synap.co.kr/problem=3
// https://projecteuler.net/problem=3

#include <stdio.h>
 
int run();
 
int main()
{
    return run();
}
 
int run()
{
    long long number = 600851475143;
    long long pf = 3;
    long long max = -1;
 
    while (number > 1)
    {
        if (number % pf == 0)
        {
            number /= pf;

            if (max < pf) { max = pf; }
        }
        else
        {
            ++pf;
        }
 
    }
 
    printf("%lld\n", max);
 
    return 0;
}
