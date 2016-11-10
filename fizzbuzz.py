
def Done(x):
	if x > 1000:
		return
	elif x % 3 == 0 and x % 5 == 0:
		print 'FizzBuzz!'
	elif x % 3 == 0:
		print 'Fizz!'
	elif x % 5 == 0:
		print 'Buzz!'
	else:
		print x	

	Done(x + 1)		

Done(2)		