// https://www.acmicpc.net/problem/1904
//20210216

#include<stdio.h>

int main()
{
	int arr[41] = { 0, 1, };
	int t, i;
	scanf("%d", &t);
	for (i = 2; i < 41; i++) arr[i] = arr[i - 1] + arr[i - 2];

	while (t-- > 0)
    {
		scanf("%d", &i);
		switch (i)
        {
		case 0:
			puts("1 0");
			break;
		case 1:
			puts("0 1");
			break;
		default:
			printf("%d %d\n", arr[i - 1], arr[i]);
		}
	}

	return 0;
}
