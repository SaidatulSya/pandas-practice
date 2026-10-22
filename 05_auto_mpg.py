# pandas_exercises 05 Merge - Auto MPG
import pandas as pd
import numpy as np

# Step 2. Import the first dataset cars1 and cars2.
url1 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv'
url2 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv'

# Step 3. Assign each to a variable called cars1 and cars2
cars1 = pd.read_csv(url1)
cars2 = pd.read_csv(url2)

# Step 4. Oops, it seems our first dataset has some unnamed blank columns, fix cars1
cars1 = cars1.dropna(axis=1, how='all')

# Step 5. What is the number of observations in each dataset?
# print(cars1.shape[0])
# print(cars2.shape[0])

# Step 6. Join cars1 and cars2 into a single DataFrame called cars
cars = pd.concat([cars1, cars2], ignore_index=True)
# print(cars)

# Step 7. Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.
owners = pd.Series(np.random.randint(15000, 73001, size=len(cars)))

# Step 8. Add the column owners to cars
cars['owners'] = owners
print(cars)
