from sys import argv
from collections import defaultdict

def unpack(path):
	working_file = open(path)

	working_list = []

	for line in working_file:
		word = line.strip()
		working_list.append(word)
	return working_list

def iter_list(working_list):

	working_set = set(working_list)
	working_dict = {}

	counter = 0
	while counter < len(working_list):
		for i in range(len(working_list[counter])):
				for j in range(i+2, (len(working_list[counter])+1)):
					# print working_list[counter][i:j]
					if working_list[counter][i:j] in working_set:
						working_dict.setdefault(working_list[counter], 0) + 1 #not working
		counter += 1

	return working_dict.items()

def return_max(final_list):
	output = max(final_list, key=lambda x: x[1])
	return output

def main(input_file):
	working_list = unpack(input_file)
	words_with_count = iter_list(working_list)
	list_most_words = return_max(words_with_count)
	print list_most_words

if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)
