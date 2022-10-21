def series_resistance(lst):
	sum_lst = sum(lst)
	if sum_lst <= 1:
		return str(sum_lst) +" " + "ohm"
	else:
		return str(sum_lst) +" " + "ohms"
