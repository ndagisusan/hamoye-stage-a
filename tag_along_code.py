import pandas as pd
import numpy as np

food_df = pd.read_csv("Stage A/FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding = "latin-1")
pd.set_option('display.max_columns', None)

# Q3: Areas that had the highest sum in 2017
print(food_df.groupby('Area')[['Y2017', 'Area']].sum())

# Q4: Year with the least correlation with ‘Element Code’
print(food_df.corr())

# Q5: The mean and standard deviation for the year 2017
print(food_df.mean())
print(food_df.std())

# Q6: The total Protein supply quantity in Madagascar in 2015
madagascar_protein_df = food_df.loc[(food_df["Area"] == "Madagascar") & (food_df["Element"] == "Protein supply quantity (g/capita/day)")]
print(madagascar_protein_df["Y2015"].sum())

# Q7: Total number and percentage of missing data in 2014
blanks_2014 = food_df['Y2014'].isnull().sum()
blanks_2014_percent =  (blanks_2014 / food_df.shape[0]) * 100
print(blanks_2014, blanks_2014_percent)

# Q14: Total number of unique countries
print(len(food_df['Area'].unique()))

# Q15
arr = np.array([[94, 89, 63],
                [93, 92, 48],
                [92, 94, 56]])

print(arr[:2, 1:])

# Q16: Year that has the highest sum of Stock Variation
print(food_df.groupby('Element').sum())

# Q17:  Area that had the 7th lowest sum in 2017
areas = food_df.groupby('Area')[['Y2017', 'Area']].sum()
print(areas.sort_values('Y2017', ascending = True).reset_index())

# Q18: Total sum of Wine produced in 2015 and 2018 
print(food_df.groupby('Item')[['Y2015', 'Y2018']].sum())

# Q19: Total number of the sum of Processing in 2017
print(food_df.groupby('Element')['Y2017'].sum())