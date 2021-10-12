"""This is the code file for problem set 1."""
import math

# Part 1
print("Hello World!")

# Part 2
# Problem 1
# Returns Bill's total wealth after 10 years where
# he deposits $1000 with annual interest rate of 5%.
deposit_amount = float(input("Enter your deposit amount: "))
desired_rate = float(input("Enter your annual interest rate: "))


def total_wealth(principle, interest_rate, duration):
    """
    Takes principle, annual interest rate and duration,
    returns eventual amount of wealth after compound interest.
    """
    return principle * (1 + float(interest_rate)) ** duration


YEARS = 10
bill_wealth = total_wealth(deposit_amount, desired_rate, YEARS)
print(f"Bill’s total wealth is ${str(round(bill_wealth, 2))}")

# Problem 2
# Return how long it take to double Bill's money at the 5%
# interest rate.
deposit_amount = float(input("Enter your deposit amount: "))
desired_rate = float(input("Enter your annual interest rate: "))


def time(interest_rate):
    """
    Takes interest rate, returns time it takes for
    principle to double. Based on formula A = P(1+r)^t.
    """
    return math.log(2) / math.log(1 + interest_rate)


bill_time = time(desired_rate)
print(f"It takes {str(round(bill_time, 2))} years to double Bill’s money.")

# Problem 3
# Return true or false on whether Jack's money will double in
# 6 years with an annual interest rate at 20%.
desired_rate = float(input("Enter your annual interest rate: "))
jack_time = time(desired_rate)
if jack_time > 6:
    print(False)
else:
    print(True)

# Problem 4
# Print the following names with their money in their savings accounts.
client_list = ["Bill", 1000, "Jack", 5000, "Amy", 6700, "Cindy", 5699, "Harry", 6700]
print(client_list)

# Problem 5
# Converting the list in the previous problem into a dictionary.
client_list_names = client_list[::2]
client_list_money = client_list[1::2]
Accounts = dict(zip(client_list_names, client_list_money))
print(Accounts)

# Problem 6
# Converting the dictionary in the previous problem into a list of key-value pair tuples.
tuples = list(Accounts.items())
print(tuples)

# Problem 7
# Lists, dictionaries and sets are all iterables that allow us to store data in them.
# Lists and sets are similar in that they are both mutable. The difference between
# them is that lists allow for duplicates and consist of ordered collection of data
# while sets don't allow duplicates and consist of unordered collection of data.
# Dictionaries are similar with sets in that they also store unordered data, but the
# main difference compared to sets is that they store data in key-value pairs while
# lists store data using indices.
