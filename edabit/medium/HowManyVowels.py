def count_vowels(txt):
	vowels = 0
	for i in txt:
			if i in 'aeiou':
				vowels = vowels + 1
	return vowels