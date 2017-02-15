def even_fibonacci_nums():
	even_sum = 0
	first_num = 1
	second_num = 2
	while second_num <= 4000000:
		if second_num % 2 == 0:
			even_sum += second_num
		first_num = second_num
		second_num = first_num + second_num
	print(even_sum)

even_fibonacci_nums()
