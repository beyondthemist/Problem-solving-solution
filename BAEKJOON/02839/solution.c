// https://www.acmicpc.net/problem/2839

#include <stdio.h>
 
int run();
 
int main()
{
    return run();
}
 
int run()
{
    int n; //3 <= n <= 5000
    int count = 0;
    int answer = 5001;
 
    scanf("%d", &n);
 
    if (n % 5 == 0) { answer = n / 5; }
    else
    {
        while (n >= 3)
        {
            if ((n % 3 == 0) && (answer > (count + n / 3))) { answer = count + n / 3; }
 
            n -= 5, ++count;
        }
    }
 
    printf("%d\n", (answer == 5001) ? -1 : answer);
 
    return 0;
}
