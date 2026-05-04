# eda -- 3 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Zomato-data-.csv')

# headline
print(df.head(20))

# columns
for i in df.columns :
    print(i)
    
# describtion
print(df.describe())

# check null value 
print(df.isna().sum())

# check duplicate
print(df.duplicated().sum())

#  data have zero null value or zero duplicate value
df['rate'] = df['rate'].str.replace('/5', '').astype(float)


# 1.Online Order
sns.countplot(x='online_order',data= df , color='green')
plt.title('online zomato service')
plt.show()
# Most restaurants 
# (~90) don't accept online orders vs ~58 that do. Majority are not online-enabled.


# 2.Book Table
sns.countplot(x='book_table',data= df , color='yellow')
plt.title('book table online')
plt.show() 
# Table booking is extremely rare — only ~8 restaurants offer it vs ~140 
# that don't.


# 3.Restaurant Type
count_ = df['listed_in(type)'].value_counts()
plt.pie(count_.values, labels=count_.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('% for each TYPES')
plt.show()
# Dining dominates at 74.3%,
# Cafes at 15.5%. Buffet and Other are negligible.


# 4.Top 10 Rated
plt.figure(figsize=(15,7))
highest_rate_resturant = df.nlargest(10,'rate')
sns.barplot(x = 'rate', y = 'name' ,data= highest_rate_resturant)
plt.show()
# Onesta leads at ~4.6.
# Rest cluster tightly between 4.2–4.45 with little difference.


# 5.Ratings Distribution
plt.figure(figsize=(10,6))
sns.histplot(x ='rate', data= df ,color= 'black')
plt.title('RATINGS')
plt.show()
# Normal-shaped distribution peaking at 3.5–3.75.
# Most restaurants are average-to-good, very few extremes.


# 6.Cost by Type
bar_value = df.groupby('listed_in(type)')['approx_cost(for two people)'].sum()
print(bar_value)
sns.barplot(data= bar_value , color= 'red')
plt.xlabel('Types')
plt.show()
# Dining has the highest total cost (~39k) — expected since it's 74% of dataset.
# Others are far behind.


#  7.Most Voted
plt.figure(figsize=(10,9))
top_resturant = df.nlargest(10, 'votes')
sns.barplot(x ='name' ,  y = 'votes', data= top_resturant)
plt.xticks(rotation = 45)
plt.show()
# Empire Restaurant (~4900) 
# and Meghana Foods (~4400) dominate. Sharp drop after top 2.


#  8.Most Expensive
plt.figure(figsize=(12,8))
expensive_resturant = df.nlargest(5,'approx_cost(for two people)')
sns.barplot(x = 'name', y = 'approx_cost(for two people)', data= expensive_resturant)
plt.xticks(rotation = 45, ha = 'right')
plt.show()
# Ayda Persian Kitchen tops at ~950 for two. 
# Top 5 are closely priced between 845–950.



