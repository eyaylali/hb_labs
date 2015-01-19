def check_payment_difference(cust_name, num_melons, amount_paid, melon_cost = 1.00):
	total_cost = melon_cost * num_melons

	if amount_paid < total_cost:
		print cust_name, "paid %.2f, %.2f less than total cost of %.2f" % (amount_paid, (total_cost-amount_paid), total_cost)
		return False
	elif amount_paid > total_cost:
		print cust_name, "paid %.2f, %.2f more than total cost of %.2f" % (amount_paid, (amount_paid-total_cost), total_cost)
		return False
	else:
		return True


def check_file(path):
	the_file = open(path)
	incorrect_payments = []

	for line in the_file:
		line = line.rstrip()

		cust_id, cust_name, num_melons, amount_paid = line.split(",")
		num_melons = int(num_melons)
		amount_paid = float(amount_paid)

		if check_payment_difference(cust_name, num_melons, amount_paid) == False:
			incorrect_payments.append([cust_name,num_melons,amount_paid])

	print
	print "Running list:"

	return incorrect_payments

print check_file("customer_orders.csv")


