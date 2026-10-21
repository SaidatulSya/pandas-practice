# pandas_exercises 04 Apply - Students Alcohol Consumption
import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'

# Step 3. Assign it to a variable called df.
df = pd.read_csv(url)
# print(df)

# Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
sliced_df = df.loc[:, 'school':'guardian'].copy()
# print(sliced_df.head())

# Step 5. Create a lambda function that will capitalize strings.
capitalize_lambda = lambda s: s.capitalize()

# Step 6. Capitalize both Mjob and Fjob
sliced_df['Mjob'] = sliced_df['Mjob'].apply(capitalize_lambda)
sliced_df['Fjob'] = sliced_df['Fjob'].apply(capitalize_lambda)


# Step 7. Print the last elements of the data set.
# print(sliced_df.tail(1))


# Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
# .apply() function does not affect the original dataframe. It returns a new Series
# Only by assigning the new value back into the column changes the original value: eg: sliced_df['Mjob'] =.apply()

# Step 9. Create a function called majority that returns a boolean value
# to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(age):
    return age > 17


sliced_df['legal_drinker'] = sliced_df['age'].apply(majority)


# print(sliced_df.head())

# Step 10. Multiply every number of the dataset by 10.
def multiply(x):
    if isinstance(x, (int, float)) and not isinstance(x, bool):
        return x * 10
    else:
        return x


new_df = sliced_df.map(multiply)

print(new_df.head())
