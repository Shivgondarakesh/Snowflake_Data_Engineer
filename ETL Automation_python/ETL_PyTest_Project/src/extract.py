import pandas as pd

def read_customers(path):
    return pd.read_csv(path)

def read_orders(path):
    return pd.read_csv(path)


def read_Employee(path):
    return pd.read_csv(filepath_or_buffer=path)

def read_department(path):
    return pd.read_csv(path)
