from sys import argv
import string
from operator import itemgetter

def unpack(input_file): 

    opened_file = open(input_file)

    words = []

    for line in opened_file:
        line = line.translate(string.maketrans("",""), string.punctuation)
        line = line.strip().lower()
        words += line.split(" ")

    opened_file.close()    
    return words  

def tally(words):
    tally_count_dict = {}
    for word in words:
        if word in tally_count_dict:
            tally_count_dict[word] += 1
        else:
            tally_count_dict[word] = 1

    return tally_count_dict
    # tally_count = {word:(tally_count[word]+1 if word in tally_count else 1) for word in words}

    

def sort_by_freq(tally_count_dict):
    desc = sorted(tally_count_dict.items())
    desc = sorted(desc, key = itemgetter(1), reverse = True)
    sorted(desc, key = itemgetter(0))
    return desc
    # desc = sorted(desc,key=lambda (x,y):(-y,x))

def print_output(freq_sorted):
    for word in freq_sorted:
        key, value = word
        print key, value

def main(input_file):
    unpacked = unpack(input_file)
    tally_count_dict = tally(unpacked)
    freq_sorted = sort_by_freq(tally_count_dict)
    print_output(freq_sorted)

if __name__ == "__main__":
    script, input_file = argv
    main(input_file)