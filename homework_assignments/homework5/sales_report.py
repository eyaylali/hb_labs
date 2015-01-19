"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

def melon_results(path):
    the_file = open(path)
    melon_results = {}

    for line in the_file:
        line = line.rstrip()
        sales_info = line.split(",")

        sales_rep = sales_info[0]
        revenue = float(sales_info[1])
        melons_sold = int(sales_info[2])

        if sales_rep in melon_results:
            melon_results[sales_rep] += melons_sold
        else:
            melon_results[sales_rep] = melons_sold
    print list(melon_results.items())

def revenue_results(path):
    the_file = open(path)
    revenue_results = {}

    for line in the_file:
        line = line.rstrip()
        sales_info = line.split(",")

        sales_rep = sales_info[0]
        revenue = float(sales_info[1])
        melons_sold = int(sales_info[2])
    

        if sales_rep in revenue_results:
            revenue_results[sales_rep] += revenue
        else:
            revenue_results[sales_rep] = revenue
    print list(revenue_results.items())

def main(sort_by,path):
    if sort_by == "melons":
        melon_results(path)
    elif sort_by == "revenue":
        revenue_results(path)
    else:
        print "Please enter valid sorting type."

main("melons", "sales_report.csv")








# salespeople = []
# melons_sold = []



# f = open("sales_report.csv")
# for line in f:
#     line = line.rstrip()
#     entries = line.split(",")
#     salesperson = entries[0]
#     melons = int(entries[2])

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print "%s sold %d melons" % (salespeople[i], melons_sold[i])
