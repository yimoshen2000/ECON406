# Problem Set 1
# Part 1
print("Hello World!")

# Part 2
# Problem 1
# Need function that takes deposit amount and interest rates as inputs and return total wealth after 10 years.
# Ask for user input
deposit_amount = float(input("What is your deposit amount:"))
annual_rate = float(input("What is the annual interest rate:"))


# Function for calculating wealth
def total_wealth(principle, int_rate, duration):
    return principle * (1 + int_rate) ^ duration


years = 10
billWealth = total_wealth(deposit_amount, annual_rate, years)
print("Bill’s total wealth is $" + billWealth)

# Problem 2
# Function for calculating duration it takes to double wealth with given interest rate

