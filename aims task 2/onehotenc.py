import pandas as pd
data = {'colour': ['Red', 'Green', 'Blue',]}
df = pd.DataFrame(data)
df_one_hot = pd.get_dummies(df, columns=['colour'],)

print(df_one_hot)