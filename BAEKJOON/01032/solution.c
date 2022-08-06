#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int num;
    int i, j;
    char input[50][51];
    char result[51];

    scanf("%d", &num);

    //Input
    for(i = 0; i < num; ++i)
        scanf("%s", input[i]);

    strcpy(result, input[0]);

    //Comparation
    for(i = 0; i < num; ++i)
    {   
        for(j = 0; j < strlen(input[i]); ++j)
        {   
            if(input[0][j] != input[i][j])
            {   
                result[j] = '?';
            }   
        }
    }   
    
    printf("%s\n", result);

    return 0;
}
