#include <stdio.h>
 
int run();
 
int main()
{
    return run();
}
 
int run()
{
    int x1, y1, r1, x2, y2, r2;
    int r3;
    int num;
    int diff;
 
    scanf("%d", &num);
 
    while(num--)
    {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
 
        r3 = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1);
        diff = r2 - r1;
 
        if (diff < 0) { diff *= -1; }
 
        if (r3)
        {
            if ((diff*diff < r3) && (r3 < (r1 + r2)*(r1 + r2))) { printf("2\n"); }
            else if ((r3 == diff*diff) || (r3 == (r1 + r2)*(r1 + r2))) { printf("1\n"); }
            else { printf("0\n"); }
        }
        else
        {
            if (r1 == r2) { printf("-1\n"); }
            else { printf("0\n"); }
        }
    }
 
    return 0;
}
