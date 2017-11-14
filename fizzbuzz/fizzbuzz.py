def fizzBuzz():
	x = 0
	while x <= 100:
		if (x % 3 == 0) and (x % 5 == 0):
			x = x +1
			print('fizzbuzz')
			
		elif (x % 3 == 0) and not (x % 5 == 0):
			x = x +1
			print('buzz')
			
		elif not (x % 3 == 0) and (x % 5 == 0):
			x = x + 1
			print('fizz')
			
		else:
			x = x +1
			print(x)
			
print(fizzBuzz())