"""This is the code file for both portions of problem set 5."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm


# Exercise 1
def first_exercise():
    """
    This function loads and preps the dataset that contains information about
    expected wage rates and its related variables. It also generates visuals
    that describe the relationship between wage and years of education. It
    also generates a model for wage data and estimates such model by producing
    an OLS regression table.
    """
    # Part 1
    wage = pd.read_csv("wage.csv").dropna()
    # Part 2
    sns.lmplot(x='educ', y='wage', data=wage)
    fig1 = plt.figure(1)
    fig1.savefig("1_2_1.png")
    sns.lmplot(x='exper', y='wage', data=wage)
    fig2 = plt.figure(2)
    fig2.savefig("1_2_2.png")
    sns.lmplot(x='tenure', y='wage', data=wage)
    fig3 = plt.figure(3)
    fig3.savefig("1_2_3.png")
    # Part 5
    lhs = wage['wage']
    ind_vars = ['educ', 'exper', 'tenure', 'nonwhite', 'female']
    rhs = wage.loc[:, ind_vars]
    rhs = sm.add_constant(rhs)
    mod = sm.OLS(lhs, rhs)
    res = mod.fit()
    print(res.summary())
    # Part 8
    hypo = pd.DataFrame({"wage": [150], "exper": [100], "tenure": [50],
                         "educ": [100], "female": [0], "nonwhite": [0]})
    print(res.predict(hypo))


# Exercise 2
def second_exercise():
    """
    This function loads and preps the dataset that contains information about
    diabetes rates and its related variables. It also generates visuals
    that describe the relationship between diabetes and variables like insulin
    levels, pedigree and glucose. It also generates a model for diabetes data
    and estimates such model by producing a logistic regression table.
    """
    # Part 1
    diabetes = pd.read_csv("diabetes.csv").dropna()
    diabetes['diabetes'] = diabetes.diabetes.map({'pos': 1, 'neg': 0})
    # Part 2
    sns.lmplot(x="insulin", y="diabetes", data=diabetes, logistic=True)
    fig4 = plt.figure(4)
    fig4.savefig("2_2_1.png")
    sns.lmplot(x="pedigree", y="diabetes", data=diabetes, logistic=True)
    fig5 = plt.figure(5)
    fig5.savefig("2_2_2.png")
    sns.lmplot(x="glucose", y="diabetes", data=diabetes, logistic=True)
    fig6 = plt.figure(6)
    fig6.savefig("2_2_3.png")
    # Part 5
    lhs = diabetes['diabetes']
    ind_vars = ['pregnant', 'glucose', 'pressure', 'triceps',
                'insulin', 'mass', 'pedigree', 'age']
    rhs = diabetes.loc[:, ind_vars]
    rhs = sm.add_constant(rhs)
    mod = sm.Logit(lhs, rhs)
    res = mod.fit()
    print(res.summary())
    # Part 7
    for percentiles in [.25, .5, .75]:
        values = rhs.quantile(percentiles)
        print(res.predict(values.to_numpy()))
        