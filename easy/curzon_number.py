def is_curzon(num):
	curzon_a = 2** num + 1
	curzon_b = 2 * num + 1
	if curzon_a % curzon_b == 0:
		return True
	else:
		return False
