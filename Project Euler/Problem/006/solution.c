// https://euler.synap.co.kr/problem=6
// https://projecteuler.net/problem=6

#include <stdio.h>
 
#define MAX 100
 
int main()
{
    printf("Square of sum: %d\n", ((((MAX)*(MAX + 1)) / 2)*(((MAX)*(MAX + 1)) / 2)));
    printf("Sum of squares: %d\n", ((MAX*(MAX + 1)*(2 * MAX + 1)) / 6));
    printf("Answer: %d\n", ((((MAX)*(MAX + 1)) / 2)*(((MAX)*(MAX + 1)) / 2)) - ((MAX*(MAX + 1)*(2 * MAX + 1)) / 6));
  
    /* another solution */
    /*
    int i;
    int answer = 0;
 
    for (i = 1; i <= MAX; ++i) { answer += ((i * i * i) - (i * i)); }
 
    printf("Answer: %d\n", answer);
    */ 
    return 0;
}
