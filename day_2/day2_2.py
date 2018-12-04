from day2_data import DATA as DATA

def count_diffs(word_a, word_b):
	diffs = 0
	for a,b in zip(word_a , word_b):
		if a != b:
			diffs += 1

	return diffs

def remove_diff(word_a, word_b):
	rem = ""
	for a,b in zip(word_a , word_b):
		if a == b:
			rem += a
  
	return rem

def main(data):
	for i in data:
		for j in data:
			if count_diffs(i, j) == 1:
				print i + " and " + j + " differ by 1 letter, Remainder is " + remove_diff(i, j)  
				return 

if __name__ == "__main__":
	main(DATA) 