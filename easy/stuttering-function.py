def stutter(word):
	ellipsis = "... "
	question = "?"
	arg = word[slice(0,2)]
	arg2 = word[slice(0,2)]
	result = arg + ellipsis + arg2 + ellipsis + word + question
	return result
