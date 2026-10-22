# pandas_exercises 05 Merge - Fictitious Names
import pandas as pd

# Step 2. Create the 3 DataFrames based on the following raw data
raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

# pd.concat - glues table together by position: stack below or put beside
# depending on axis=0(stack below), axis=1(put beside)
# Step 4. Join the two dataframes along rows and assign all_data
all_data = pd.concat([data1, data2], ignore_index=True)
# print(all_data)

# Step 5. Join the two dataframes along columns and assigned to all_data_col
all_data_col = pd.concat([data1, data2], axis=1)
# print(all_data_col)

# Step 6. Print data3
# print(data3)

# Step 7. Merge all_data and data3 along the subject_id value
all_data_d3 = pd.merge(all_data, data3, on='subject_id')
# print(all_data_d3)

# Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2
merge_subject_id = pd.merge(data1, data2, on='subject_id', how='inner')
# print(merge_subject_id)

# Step 9. Merge all values in data1 and data2, with matching records from both sides where available.
# print(data1)
# print(data2)

merge_data1_data2 = pd.merge(data1, data2, on='subject_id',how='outer')
print(merge_data1_data2)
