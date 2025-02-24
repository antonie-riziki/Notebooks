import pandas as pd
import numpy as np
import seaborn as sb
import os
from collections import defaultdict, Counter
import sys
import matplotlib.pyplot as plt

"""
dparser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %I-%p")
df = pd.read_csv("D:\Open Classroom\Ethereum\ETH_1h.csv", parse_dates = ["Date"], date_parser = dparser)
"""
df = pd.read_csv("D:\Open Classroom\Ethereum\ETH_1h.csv")
df["Date"] = pd.to_datetime(df["Date"], format = "%Y-%m-%d %I-%p")
df.drop(columns = ["Unnamed: 0"], inplace = True)
print(df.loc[1509, "Date"])

df["WeekDay"] = df["Date"].dt.day_name()
print(df.head(10))
print()
print()
print(df["High"].resample("m").max())
df["Date"].dt.is_leap_year('2020-02-29')
