store_sales = [12000, 18000, 9000, 25000, 16000]

# Store target check
store_number = 1

for sales in store_sales:
    if sales <= 15000:
        print("Store", store_number, "did not achieve")
    else:
        print("Store", store_number, "did achieve")

    store_number = store_number + 1

print("----------------------------")

# Stores above 20,000
for sales in store_sales:
    if sales > 20000:
        print(sales)

print("----------------------------")

# Total Sales
total_sales = 0

for sales in store_sales:
    total_sales += sales

print("Total Sales:", total_sales)

print("----------------------------")

# Average Sales
avg_sales = total_sales / len(store_sales)

print("Average Sales:", avg_sales)

print("----------------------------")

# Highest Sales
highest_sales = 0

for sales in store_sales:
    if sales > highest_sales:
        highest_sales = sales

print("Highest Sales:", highest_sales)

print("----------------------------")

# Lowest Sales
lowest_sales = store_sales[0]

for sales in store_sales:
    if sales < lowest_sales:
        lowest_sales = sales

print("Lowest Sales:", lowest_sales)

print("----------------------------")

# Final Report
print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)