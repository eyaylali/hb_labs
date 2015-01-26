# !/usr/bin/env python


from sys import argv
import random

ENDING_PUNCTUATION = ["?", ".", "!"]


def unpack_file(input_file_1, input_file_2):
    file_object_1 = open(input_file_1)
    file_object_2 = open(input_file_2)

    word_bank_list = []
    for line in file_object_1:
        line = line.rstrip().translate(None, "()").split()
        word_bank_list += line
    for line in file_object_2:
        line = line.rstrip().translate(None, "()").split()
        word_bank_list += line
    return word_bank_list


def make_chains(word_bank_list):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""


    markov_dict_final = {}

    for i in range(len(word_bank_list)-2):
        key = (word_bank_list[i], word_bank_list[i+1])

        if key not in markov_dict_final:
            markov_dict_final[key] = [word_bank_list[i+2]]
        else:
            markov_dict_final[key] = markov_dict_final[key] + [word_bank_list[i+2]]

    return markov_dict_final


def make_text(markov_dict_final):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    random_key = random.choice(markov_dict_final.keys())
    tuple_at_0 = random_key[1].translate(None, ".")
    tuple_at_1 = random.choice(markov_dict_final[random_key]).translate(None, ".")
    markov_text = [tuple_at_0, tuple_at_1]
    character_length = (len(tuple_at_0) + len(tuple_at_1))
    
    while True:
        search_tuple = (markov_text[-2],markov_text[-1])
        if search_tuple in markov_dict_final:
            next_word_options = markov_dict_final[search_tuple]
            next_word = random.choice(next_word_options)
            markov_text.append(next_word)
            character_length += (len(next_word) + 1)
            if next_word[-1] in ENDING_PUNCTUATION or character_length >= 130:
                break
        else:
            break

    markov_text[0] = markov_text[0].title()
    markov_text[1] = markov_text[1].lower()
    markov_output = " ".join(markov_text).lower()
    return markov_output
    

def main(input_file_1, input_file_2):
    word_bank_list = unpack_file(input_file_1, input_file_2)
    markov_dict_final = make_chains(word_bank_list)
    returned_text = make_text(markov_dict_final)
    return returned_text
 

if __name__ == "__main__":
    input_file_1 = argv[1]
    input_file_2 = argv[2]
    main(input_file_1, input_file_2)