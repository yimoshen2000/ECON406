"""This is the code file for the demand exercise portion of HW2."""
import math


# Part a
def compute_elasticity(price1: float, price2: float, quant1: float, quant2: float) -> float:
    """
    This function calculates an elasticity based on the
    taylor-series approximation form for a given input of two
    prices and two quantities.
    """
    return math.log(quant2/quant1) / math.log(price2/price1)


# Part b
def check_elasticity(elasticity: float) -> str:
    """
    This function returns whether an elasticity is elastic,
    inelastic or unit-elastic.
    """
    elasticity = abs(elasticity)
    if elasticity > 1:
        result = str("elastic")
    elif elasticity == 1:
        result = str("unit-elastic")
    else:
        result = str("inelastic")
    return result


# Part c
def compute_demand(sales: float, init_price: float, new_price: float, elasticity: float) -> float:
    """
    This function takes initial sales of a product, an initial
    price, a new price, and an elasticity and calculates the
    predicted demand at the new price.
    """
    predicted_demand = sales * (new_price / init_price)**elasticity
    return predicted_demand


# Part d
def main():
    """
    This function asks the user whether to calculate either
    elasticity or demand.
    """
    answer = input("Calculate elasticity or demand?")
    if answer == "elasticity":
        old_price = float(input("Enter old price: "))
        new_price = float(input("Enter new price: "))
        old_quantity = float(input("Enter old quantity: "))
        new_quantity = float(input("Enter new quantity: "))
        calculated_elasticity = compute_elasticity(old_price, new_price, old_quantity, new_quantity)
        elasticity_status = check_elasticity(calculated_elasticity)
        print(f"New elasticity: {str(calculated_elasticity)}; {str(elasticity_status)}")
    elif answer == "demand":
        sales_quantity = float(input("Enter sales quantity: "))
        initial_price = float(input("Enter initial price: "))
        elasticity = float(input("Enter elasticity: "))
        price_points_num = int(input("Enter number of new price points: "))
        demand_dictionary = dict()
        i = 0
        for _ in range(price_points_num):
            i += 1
            new_price = float(input(f"Enter new price #{str(i)}: "))
            new_demand = compute_demand(sales_quantity, initial_price, new_price, elasticity)
            demand_dictionary[new_price] = new_demand
        print(demand_dictionary)
    else:
        print("Invalid input!")
        main()
        