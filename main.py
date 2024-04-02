import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url = "C:\\Users\\User\\Desktop\\ML Projects\\Amazon-Recommender-System\\ratings_Electronics.csv"
data = pd.read_csv(url, names = ['User', 'Id', 'Rating', 'Timestamp'])

# First look at data
# print(data.head())
# print(data.shape)
# print(data.dtypes)

# Check if there are any missing data
# print(data.isnull().sum())

# Checking rating distribution
# print(data['Rating'].unique())
tally = []
rating = np.sort(data['Rating'].unique())
for i in rating:
    tally.append((data['Rating'] == i).sum())
# plt.bar(rating, tally)
# plt.show()

# Removing unessecary data (columns)
data.drop(['Timestamp'], axis = 1, inplace = True)

# Rating analysis first look
user = data['User'].unique()
# print(user.size)
prod_per_user = data.groupby(by = 'User')['Rating'].count().sort_values(ascending = False)
# print(prod_per_user.head())


# -----Popularity based system-----
# New dataframe with users who have rated 50 or more items.
popsys = data.groupby(by = 'Id').filter(lambda x:x['Rating'].count() >= 50)
# print(popsys.head())

# Number of ratings for each product
rating_no = popsys.groupby(by = 'Id')['Rating'].count().sort_values(ascending = False)
# print(rating_no.head())

# Average rating of each product
# print(popsys.groupby(by = 'Id')['Rating'].mean().sort_values(ascending = False).head())

# Total number of ratings for each product
# print(popsys.groupby('Id')['Rating'].count().sort_values(ascending = False).head())

avg_ratings = pd.DataFrame(popsys.groupby(by = 'Id')['Rating'].mean())
avg_ratings['Rating Count'] = pd.DataFrame(avg_ratings.groupby('Id')['Rating'].count())
# print(avg_ratings.head())