from math import gcd as bltin_gcd

def coprime(a, b):
    return bltin_gcd(a, b) == 1

def line_generator_1(m):
	for i in range(0,m):
		k = (i*4) % m
		print(f"$x = {i}$; $6 \\equiv 4({i})$(mod ${m}) \\equiv {k}$\\newline")

def line_generator_2(m):
		for i in range(1,m+1):
			gcd = coprime(i,m)
			print(f"$({i},{m}) = {bltin_gcd(i,m)}\\Rightarrow$ multiplicative inverse {gcd}.\\newline")


line_generator_2(12)