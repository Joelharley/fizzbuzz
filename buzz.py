
for i in range(1,100):
	if float(i) % 3 == 0.0 and float(i) % 5 == 0.0:
		print('fizzbuzz')
	elif float(i) % 3 == 0.0 and float(i) % 5 != 0.0:
		print('fizz')
	elif float(i) % 5 == 0.0 and float(i) % 3 != 0.0:
		print('buzz')
	else:
		print(i)
