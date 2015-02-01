from sys import argv

def main(input_file):

	def count_of_subwords(word):
		return sum(word[i:j] in words for i in range(len(word)-1) for j in range(i+ 2, len(word) +1))

	words = {word.strip() for word in open(input_file)}
	print max(words, key=count_of_subwords)

if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)

