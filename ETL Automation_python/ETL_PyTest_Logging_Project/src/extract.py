import pandas as pd
from logger import logger

def read_customers(path):
 logger.info(f"Reading {path}")
 return pd.read_csv(path)

def read_orders(path):
 logger.info(f"Reading {path}")
 return pd.read_csv(path)
