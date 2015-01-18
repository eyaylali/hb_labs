def print_output(csv):
    my_file = open(csv)
    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
    
        melon = words[0]
        count = words[1]
        amount = words[2]
    
        print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
    my_file.close()

# Day 1
print "Day 1"
print_output("um-deliveries-20140519.csv")

# Day 2
print "Day 2"
print_output("um-deliveries-20140520.csv")

# Day 3
print "Day 3"
print_output("um-deliveries-20140521.csv")

