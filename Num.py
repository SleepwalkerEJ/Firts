def is_prime(x):
	for i in range(2, x/2 + 1): #Por cada numero del 2 al 100
		if x % i == 0:
			return False
	return True


print [is_prime (i) for i in range(2,100)]