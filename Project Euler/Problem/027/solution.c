// https://euler.synap.co.kr/problem=27
// https://projecteuler.net/problem=27

#include <stdio.h>

int is_prime(int num);

int main() 
{
	int a = 0, b = 0;
	int n = 0;
	int temp = 0;
	int max = 0;
	int res_a = 0, res_b = 0;
	long long res = 0;
	
	
	for(a = -999; a < 1000; ++a)
	{
		for(b = -999; b < 1000; ++b)
		{
			for(n = 1; ; ++n)
			{
				temp = n*n +a*n + b;
				
				if(!is_prime(temp))
				{
					break;
				}
			}
			
			if(max < n)
			{
				max = n;
				res_a = a;
				res_b = b;
			}
		}
	}
	
	res = res_a*res_b;
	
	printf("%lld", res);
	
	
	return 0;
}

int is_prime(int num)
{
	if(num < 2)
	{
		return 0;
	} 
	else
	{
		if(num == 2)
		{
			return 1;
		} 
		else
		{
			if(num % 2 == 0)
			{
				return 0;
			}
			else
			{
				for(int i = 3; (i*i) <= num; i += 2)
				{
					if(num%i == 0)
					{
						return 0;
					}
				}
				
				return 1;
			}
		}
	}
}
