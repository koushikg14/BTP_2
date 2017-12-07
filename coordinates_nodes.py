import pandas as pd
df = pd.read_csv('temp-nodes.csv')
new_df = df[['x','y','OBJECTID']]
coordinates = {}

for i,j,k in zip(df['OBJECTID'],df['x'],df['y']):
	 coordinates[i] = [j,k]
	 

