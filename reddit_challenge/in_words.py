from sys import argv

def unpack(path):
    return {w.strip() for w in open(path)}

def iter_list(working_set):

    working_dict = {}

    for counter, word in enumerate(working_set):
        for i in range(len(word) - 1):
            for j in range(i + 2, (len(word) + 1)):
                if word[i:j] in working_set:
                    working_dict[word] = working_dict.get(word, 0) + 1

    return working_dict

def return_max(final_list):
    output = max(final_list, key=lambda x: final_list[x])
    return output

def main(input_file):
    working_list = unpack(input_file)
    words_with_count = iter_list(working_list)
    list_most_words = return_max(words_with_count)
    print list_most_words

if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)


