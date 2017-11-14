def euler(number):
	count = 0
	score = 0
	while count < number:
		if (count % 15 == 0):
			count = count + 1
			score = score + count			

		elif (count % 3 == 0) and not (count % 5 == 0):
			count = count + 1
			score = score + count 		
			
		elif not (count % 5 == 0) and (count % 5 == 0):
			count = count + 1
			score = score + count
			
		else:
			count = count + 1
			score = score
		
	return score
	
print(euler(1000))
		
			
