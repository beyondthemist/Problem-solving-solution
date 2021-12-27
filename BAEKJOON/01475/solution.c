// https://www.acmicpc.net/problem/1475

#include <stdio.h>
 
int run();
 
int main()
{
    return run();
}
 
int run()
{
    int n;
    int temp;
    int i;
    int max = 0;
    int arr[9] = { 0 };
 
    scanf("%d", &n);
 
    do
    {
        temp = n % 10; n /= 10;
 
        if (temp == 9) { ++(arr[6]); }
        else { ++(arr[temp]); }
    } while (n);
 
    arr[6] = (arr[6] / 2) + (arr[6] % 2);
 
    for (i = 0; i < 9; ++i)
    {
        if (max < arr[i]) { max = arr[i]; }
    }
 
    printf("%d\n", max);
 
    return 0;
}
