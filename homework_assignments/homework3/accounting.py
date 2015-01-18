def tally_machine(path):
    my_file = open(path)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    for line in my_file:
        data = line.split(',')
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    my_file.close()
    return melon_tallies

def revenue_calculator(melon_tallies):
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

def sales_channel_filter(path):
    sales_file = open(path)
    sales = [0, 0]
    for line in sales_file:
        data = line.split(",")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    print "Salespeople generated %0.2f in revenue." % sales[1]
    print "Internet sales generated %0.2f in revenue." % sales[0]
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

# To generate the main report

path1 = "orders_by_type.csv"
path2 = "orders_with_sales.csv"

def report_generator(path1, path2):
    print "******************************************"
    melon_tallies = tally_machine(path1)
    print "******************************************"
    revenue_calculator(melon_tallies)
    print "******************************************"
    sales_channel_filter(path2)

report_generator(path1,path2)
