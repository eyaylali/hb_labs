from sys import argv

def unpack(input_file): 
    '''Takes a file and creates an item in a dictionary for each line;
    returns a sorted list of tuples (restaurant, rating)'''

    opened_file = open(input_file)
    ratings = {}

    for line in opened_file:
        line = line.strip()
        restaurant, rating = line.split(":")
        ratings[restaurant] = rating

    opened_file.close()    
    return ratings  

def print_sorted(ratings):
    ''' stuff '''

    ratings = sorted(ratings.items())  
    for i in ratings:
        print "Restaurant %s is rated at %s." % i

def main(input_file):
    '''Takes a file, passes to unpack;
    prints restaurants and ratings'''

    print_sorted(unpack(input_file))

if __name__ == "__main__":
    script, input_file = argv
    main(input_file)