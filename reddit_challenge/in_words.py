from sys import argv

    # dictionary = set(word.strip() for word in words if len(word.strip()) > 2)


def unpack(path):
	working_file = open(path)

	working_list = []

	for line in working_file:
		word = line.split()
		working_list += word
	return working_list

def iter_list(working_list):

	working_set = set(working_list)
	working_dict = {}

	counter = 0
	for i in range(len(working_list[counter])):
		if len(working_list[counter]) > 2: #not sure about placement
			for j in range(i+2, (len(working_list[counter])+1)):
				if working_list[counter][i:j] in working_set:
					dict2 = working_dict.setdefault(working_list[counter], 0) + 1
			counter += 1

	return working_dict.items()

def return_max(final_list):
	output = max(final_list, key=lambda x: x[1])
	return output

	# working_dict = {}
	# words_with_most_words = []
	# word_quantity = 0


	# counter = 0
	# checked_word = working_list[counter]

	# for word1 in (working_list[:counter] and working_list[counter:]):
	# 	if word1 in checked_word and word1 != checked_word and word1 >=2:
	# 		if checked_word in working_dict:
	# 			working_dict[checked_word] += 1
	# 			counter += 1
	# 		else:
	# 			working_dict[checked_word] = 1

	# for quantity in working_dict.values():
	# 	if quantity > word_quantity:
	# 		word_quantity = quantity

	# for word, quantity in working_dict.items():
	# 	if quantity == word_quantity:
	# 		words_with_most_words += [word]

	# return words_with_most_words, word_quantity

def main(input_file):
	working_list = unpack(input_file)
	words_with_count = iter_list(working_list)
	list_most_words = return_max(words_with_count)
	print list_most_words


if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)

