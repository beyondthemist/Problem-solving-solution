// https://www.acmicpc.net/problem/1004

#include <stdio.h>
 
int main()
{
    int t, n;
    int srcX, srcY, destX, destY;
    int cX, cY, r;
    int count;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d %d %d %d", &srcX, &srcY, &destX, &destY);
        count = 0;
        scanf("%d", &n);
        while (n--)
        {
            scanf("%d %d %d", &cX, &cY, &r);
            if ((((srcX - cX) * (srcX - cX)) + ((srcY - cY) * (srcY - cY)) <= r * r)
            != (((destX - cX) * (destX - cX)) + ((destY - cY) * (destY - cY)) <= r * r))
            {
                ++count;
            }
        }
 
        printf("%d\n", count);
    }
 
    return 0;
}
