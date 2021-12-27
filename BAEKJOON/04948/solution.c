// https://www.acmicpc.net/problem/4948

#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    int input;
    int count = 0;
    int i, j;
    int* result = (int*)malloc(sizeof(int));
    int idx = 0;
    int isComp[246913] = { 0 };
 
    for (i = 2; i < sizeof(isComp) / sizeof(int); ++i)
    {
        if (isComp[i] == 0)
        {
            for (j = 2*i; j < sizeof(isComp) / sizeof(int); j += i)
            {
                isComp[j] = 1;
            }
        }
    }
 
    while(1)
    {
        scanf("%d", &input);
        
        if (!input) { break;}
 
        for (i = (input + 1); i <= (2 * input); ++i)
        {
            if (!isComp[i])    { ++count; }
        }
 
        result = realloc(result, sizeof(int) * (idx + 1));
        result[idx++] = count;
        
        count = 0;
    } 
    
    for (i = 0; i < idx; ++i)
    {
        printf("%d\n", result[i]);
    }
    
    return 0;
}
