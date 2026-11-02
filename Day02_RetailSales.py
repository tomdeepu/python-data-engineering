
# Day 2 - Retail Sales Calculation

store_name = input("Enter Store Name: ")
monthly_sales = input("Enter Monthly Sales: ")

# Convert sales from text to number
monthly_sales = float(monthly_sales)

target_sales = 10% + int(monthly_sales)

print("\nRETAIL SALES REPORT")
print("-------------------")

print("Store:", store_name)
print("Monthly Sales:", monthly_sales)

print("Target Sales:", target_sales)

# Calculate achievement
achievement = (monthly_sales / target_sales) * 100

print("Target Achievement:", achievement, "%")

# Check target
print("Target Achieved:", monthly_sales >= target_sales)
