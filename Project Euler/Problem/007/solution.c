// https://euler.synap.co.kr/problem=7
// https://projecteuler.net/problem=7

//Not used Sieve of Eratosthenes.

#include <stdio.h>
 
int is_prime(int num);
 
int main()
{
    int i;
    int count = 2;
 
    for (i = 3; count <= 10001; i += 2)
    {
        if (is_prime(i)) { ++count; }
    }
 
    printf("answer: %d\n", (i - 2));
 
    return 0;
}
 
int is_prime(int num)
{
    int i;
 
    for (i = 3; i*i <= num; i += 2)
    {
        if (num%i == 0) { return 0; }
    }
 
    return 1;
}
