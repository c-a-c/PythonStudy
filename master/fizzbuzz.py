for i in range(1,50,2):
	flag = True

	if(i % 3 == 0):
		print("Fizz", end="")
		flag = False
	if(i % 5 == 0):
		print("Buzz", end="")
		flag = False

	txt = i if flag == True else ""
	print(txt)
