// https://www.acmicpc.net/problem/1904
#include <stdio.h>

int main()
{
    int x = 1, y = 1;
    int i = 0, temp;
    int n;

    scanf("%d", &n);
    for (; i < n - 1; ++i)
    {
        temp = x;
        x = y % 15746;
        y = (y + temp) % 15746;
    }

    printf("%d", y);

    return 0;
}
