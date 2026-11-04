
# Day 4 - Retail Store Bonus Eligibility System

# Step 1: Get store details
store_name = input("Enter Store Name: ")
monthly_sales = float(input("Enter Monthly Sales: "))
customer_rating = int(input("Enter Customer Rating (1-5): "))
is_active = input("Is Store Active? (yes/no): ").lower()

# Step 2: Display store information
print("\nRETAIL BONUS REPORT")
print("----------------------------")

print("Store Name:", store_name)
print("Monthly Sales:", monthly_sales)
print("Customer Rating:", customer_rating)
print("Store Active:", is_active)

# Step 3: Check bonus eligibility
print("\nBONUS ELIGIBILITY")
print("----------------------------")

if is_active == "yes":

    if monthly_sales >= 25000 and customer_rating >= 4:
        print("Bonus Status: APPROVED")
        print("Congratulations! Store qualifies for bonus.")

    else:
        print("Bonus Status: NOT APPROVED")

        if monthly_sales < 25000:
            print("Reason: Sales target not achieved")

        if customer_rating < 4:
            print("Reason: Customer rating is below 4")

else:
    print("Bonus Status: NOT APPROVED")
    print("Reason: Store is inactive")

print("----------------------------")
print("Analysis Completed")
