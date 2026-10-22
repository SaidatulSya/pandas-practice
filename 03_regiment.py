# pandas_exercises 03 Grouping - Regiment

# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Create the DataFrame with the following values:
raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons',
                 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
    'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani',
             'Ali'],
    'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

regiment = pd.DataFrame(data=raw_data)

# Step 4. What is the mean preTestScore from the regiment Nighthawks?
pretest_avg = regiment.groupby('regiment')['preTestScore'].mean()
# print(pretest_avg.loc['Nighthawks'])

# another approach for Step 4 question
# filter for where regiment is Nighthawks, then calculate the mean()
is_nighthawks = regiment['regiment'] == 'Nighthawks'
nh_pretest_avg = regiment[is_nighthawks]['preTestScore'].mean()  # filters the row that is True Nighthawks
# print(nh_pretest_avg)

# Step 5. Present general statistics by company
# print(regiment.groupby('company').describe().T) #transpose the wide table

# Step 6. What is the mean of each company's preTestScore?
company_pretest_avg = regiment.groupby('company')['preTestScore'].mean()
# print(company_pretest_avg.round(1))

# Step 7. Present the mean preTestScores grouped by regiment and company
comp_reg_pretest_avg = regiment.groupby(['regiment', 'company'])['preTestScore'].mean()
# print(comp_reg_pretest_avg)

# Step 8. Present the mean preTestScores grouped by regiment and company without hierarchical indexing
# print(comp_reg_pretest_avg.reset_index())

# Step 9. Group the entire dataframe by regiment and company
grouped_reg_comp = regiment.groupby(['regiment', 'company'])
# print(grouped_reg_comp.mean(numeric_only=True))

# Step 10. What is the number of observations in each regiment and company
print(grouped_reg_comp.size())

# Step 11. Iterate over a group and print the name and the whole data from the regiment
# for name, group in regiment.groupby('regiment'):
#     print(name)
#     print(group)
#     print()
