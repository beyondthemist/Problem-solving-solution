// https://euler.synap.co.kr/problem=19
// https://projecteuler.net/problem=19

#include <stdio.h>
 
int main()
{
    int day = 1; 
    int year, month;
    int count = 0;
    int is_leap;
 
    int arr[2][12] = { 
        { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 },
        { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }
    };
 
    for (month = 1; month <= 12; ++month) 
    {
        day += arr[0][month - 1];
    }
    day = 1 + (7 - (day % 7));
 
    for (year = 1901; year <= 2000; ++year) 
    {
        is_leap = ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
 
        for (month = 1; month <= 12; ++month)
        {
            count += (day == 1);
 
            while (day <= arr[is_leap][month - 1])
            {
                day += 7;
            }
 
            day -= arr[is_leap][month - 1];
        }
    }
 
    printf("%d\n", count);
 
    return 0;
}
