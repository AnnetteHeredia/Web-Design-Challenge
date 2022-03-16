import pandas as pd

# turn our csv into a dataframe.
df = pd.read_csv('cities.csv')

# Save as html, df to html
df.to_html('data.html', index=False)

# Assign to a string
table = df.to_html()
print(table)