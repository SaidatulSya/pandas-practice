# pandas_exercises 03 Grouping – Occupation (steps 4–8)
import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep='|')
# print(users.head())

# Step 4. Discover what is the mean age per occupation
# Group by Occupation and find average age
avg_age = users.groupby('occupation')['age'].mean()
avg_age_rounded = avg_age.round(0).astype(int)
# print(avg_age_rounded)

# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
# Create new column to map M:1, F:0. Then group by Occupation and use mean()
users['is_male'] = users['gender'].map({'M': 1, 'F': 0})
male_users_ratio = users.groupby('occupation')['is_male'].mean()
male_ratio_sorted = male_users_ratio.sort_values(ascending=False)
# print(male_ratio_sorted)

# Step 6. For each occupation, calculate the minimum and maximum ages
min_age = users.groupby('occupation')['age'].min()
max_age = users.groupby('occupation')['age'].max()
# print(min_age)
# print(max_age)

# Step 7. For each combination of occupation and gender, calculate the mean age
# group by occupation first, then by gender.
occ_gender_mean = users.groupby(['occupation', 'gender'])['age'].mean()
# print(occ_gender_mean)

# Step 8. For each occupation present the percentage of women and men
female_users_percent = (1 - male_users_ratio) * 100
male_users_percent = male_users_ratio * 100
gender_percent = {'female_percent': female_users_percent, 'male_percent': male_users_percent}
occ_gender_df = pd.DataFrame(data=gender_percent)
print(occ_gender_df.round(1))
