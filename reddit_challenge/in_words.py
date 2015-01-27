from sys import argv


def unpack(path):
	working_file = open(path)

	working_list = []

	for line in working_file:
		word = line.split()
		working_list += word
	return working_list

def iter_list(working_list):

	working_dict = {}
	words_with_most_words = []
	word_quantity = 0

	for word1 in working_list:
		for word2 in working_list:
			if len(word2) >= 2 and word2 in word1 and word1 != word2:
				if word1 in working_dict:
					working_dict[word1] += 1
				else:
					working_dict[word1] = 1

	for quantity in working_dict.values():
		if quantity > word_quantity:
			word_quantity = quantity

	for word, quantity in working_dict.items():
		if quantity == word_quantity:
			words_with_most_words += [word]

	return words_with_most_words, word_quantity
	

def main(input_file):
	working_list = unpack(input_file)
	most_words_word = iter_list(working_list)
	print most_words_word


if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)

