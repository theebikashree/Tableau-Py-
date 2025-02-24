import pandas as pd
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\Harry_Potter_Movies\Movies.csv")
print( df.to_string())
print(df.info())
missing_values = df.isna().sum()
print("\nMissing Values in Each Column:\n", missing_values)
print("\nDuplicate Movie IDs:", df.duplicated('Movie ID').sum())
print("\nData Summary:\n", df.describe())
df.to_csv(r'C:\Users\ADMIN\Downloads\Harry_Potter.csv', index=False)
df.to_csv(r'C:\Users\ADMIN\Downloads\python\Harry_Potter.csv', index=False)

