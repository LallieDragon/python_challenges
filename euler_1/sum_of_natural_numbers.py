def euler(number):
	total = 0
	for i in range(number):
		if (i % 3 == 0) or (i % 5 == 0):
			total = total + i		
	return total
	
print(euler(1000))
		
			
