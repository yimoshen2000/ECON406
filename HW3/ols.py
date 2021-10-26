"""This is the code file for the OLS portion of problem set 3."""
import numpy as np
import pandas as pd


def extract_variable_means(dataset_filename: str):
    """
    Calculates the mean values of the number of total campus crimes,
    employed police officers, and total college enrollment.
    """
    df1 = pd.read_csv(dataset_filename)
    df_mean = df1[["crime", "police", "enroll"]].mean()
    return df_mean


def extract_estimator(dataset_filename: str):
    """Calculates the ols estimator vector"""
    df2 = pd.read_csv(dataset_filename).dropna() # Drop any row that has missing data
    df2["beta_0"] = 1 #add column of 1s
    x_mat = df2[["beta_0","lenroll"]] # matrix x => column log-enroll and column beta_0 combined
    y_vec = df2["lcrime"] #vector y = log crime
    beta_hat=np.dot(np.linalg.inv(np.dot(np.transpose(x_mat),x_mat)),
                    np.dot(np.transpose(x_mat),y_vec))
    return beta_hat
