#include <stdio.h>
 
#define LIMIT 4000000
 
int fib(int);
 
int main()
{
    int i;
    int sum = 0;
    int temp;
 
    for (i = 1; (temp = fib(i)) <= LIMIT; ++i)
    {
        if (temp % 2 == 0) { sum += temp; }
    }
    
    printf("sum: %d\n", sum);
 
    return 0;
}
 
int fib(int n)
{
    return ((n == 0) || (n == 1)) ? n : (fib(n - 1) + fib(n - 2));
}
