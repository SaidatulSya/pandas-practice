# pandas_exercises 02 Filtering & Sorting – Euro12

# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called euro12.
euro12 = pd.read_csv(
    'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')

# Step 4. Select only the Goal column.
# pd.columns - show lists of columns
# print(euro12['Goals'])

# Step 5. How many team participated in the Euro2012? answer: 16
## - check if there is any duplicate in the list
# team_isunique = euro12['Team'].is_unique
# print(team_duplicates)

## - count Team
# team_count = euro12['Team'].nunique()
# print(team_count)
# print(euro12['Team'])

# Step 6. What is the number of columns in the dataset? answer: 35
# num_cols = euro12.shape[1]
# print(num_cols)

# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
# discipline = euro12[['Team','Yellow Cards','Red Cards']]
# print(discipline)

# Step 8. Sort the teams by Red Cards, then to Yellow Cards
# sort_discipline = discipline.sort_values(by=['Red Cards','Yellow Cards'])
# print(sort_discipline)

# Step 9. Calculate the mean Yellow Cards given per Team answer: 7.4375
# yellow_card_mean = discipline['Yellow Cards'].mean()
# print(yellow_card_mean)

# Step 10. Filter teams that scored more than 6 goals answer: Germany(10) and Spain(12)
# filtered_euro12 = euro12.loc[euro12['Goals']>6]
# print(filtered_euro12[['Team','Goals']])

# Step 11. Select the teams that start with G answer: Germany, Greece
# filtered_euro12_name = euro12.loc[euro12['Team'].str.startswith('G')]
# print(filtered_euro12_name['Team'])

# Step 12. Select the first 7 columns
# euro12_cols = euro12.iloc[:, 0:7]
# print(euro12_cols)

# Step 13. Select all columns except the last 3.
# euro12_cols_ = euro12.iloc[:, :-3]
# print(euro12_cols_)

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
## - filter row that Team name is England, Italy and Russia
team = ['England', 'Italy', 'Russia']
euro12_filtered_team = euro12[euro12['Team'].isin(team)]
print(euro12_filtered_team[['Team', 'Shooting Accuracy']])
