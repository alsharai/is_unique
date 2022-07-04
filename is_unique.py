def is_unique(word):
	"""
	Checks if a string has any duplicate letters

	>>> is_unique("unique")
	False
	>>> is_unique("code")
	True
	>>> is_unique("abcdefghijklmnopqrstuvwxyza")
	False
	"""

	n = len(word)
	checker = 0

	# pigeonhole principle
	if n > 26:
		return False

	for letter in word:
		relative_ascii_number = ord(letter) - ord('a')

		# checks if the letter has been seen
		if checker & (1 << relative_ascii_number) > 0:
			return False

		checker |= (1 << relative_ascii_number)


	return True
