files_by_day = ["um-deliveries-20140519.csv","um-deliveries-20140520.csv","um-deliveries-20140521.csv"]


def report_content(day_number, path):
    print "Day %d" % day_number
    my_file = open(path, "r")
    for line in my_file:
        line = line.rstrip()
        words = line.split(',')

        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print ("Delivered %s %ss for total of $%s" % (
            count, melon, amount)).upper()
    my_file.close()

    print

def main():
	for day in range(len(files_by_day)):
		report_content((day+1), files_by_day[day])


main()
