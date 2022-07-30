//https://www.acmicpc.net/problem/5622
//20180426

#include <stdio.h>
#include <string.h>

int main()
{
    char input[16];
    int lib[26] ={3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10};
    int i;
    int sum = 0;
    
    scanf("%s", input);

    for(i = 0; i < strlen(input); ++i)
    {   
        sum += lib[input[i] - 'A'];
    }   

    printf("%d", sum);
    
    return 0;
}
