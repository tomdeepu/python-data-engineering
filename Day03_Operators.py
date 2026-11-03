
# Day 3 - Arithmetic Operators

store_a_sales  = 25000
store_b_sales = 18000
monthly_sales = 50000
number_of_stores = 4

total_sales = store_a_sales + store_b_sales
sales_difference = store_a_sales - store_b_sales
average_sales = total_sales / 2
average_sales2 = monthly_sales / number_of_stores


print("RETAIL SALES ANALYSIS")
print("---------------------")

print("Store A Sales:", store_a_sales)
print("Store B Sales:", store_b_sales)
print("Total Sales:", total_sales)
print("Sales Difference:", sales_difference)
print("Average Sales:", average_sales2)
print(type(average_sales))
print("---------------------")
print("\n")


# Day 3 - Comparison Operators

monthly_sales = 18000
target_sales = 20000

print("Monthly Sales:", monthly_sales)
print("Target Sales:", target_sales)

print("Above Target:", monthly_sales > target_sales)
print("Below Target:", monthly_sales < target_sales)
print("Target Achieved:", monthly_sales >= target_sales)

print("---------------------")
print("\n")

monthly_sales = 30000

if monthly_sales >= 28000:
    print("Excellent")
elif  monthly_sales>= 22000:
    print("Good")
elif monthly_sales >= 17000:
    print("Average")
elif monthly_sales >= 12000:
    print("improve")