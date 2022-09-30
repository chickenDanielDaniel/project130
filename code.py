import pandas as pd
import csv

df = pd.read_csv("")
print(df.shape)
print(df.columns)

del df["Luminosity"]

print(df.shape)
print(list(df))


df.to_csv("main.csv")