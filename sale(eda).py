# sale data set eda

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv('C:\\Users\\abdulrehman1793\\Downloads\\sales_data.csv')
 
 
print('\nshape of data')
print(df.shape)

print('\nhead  of the data')
print(df.head(30))

print(df.tail(20))

print('\ninfo of the data')
print(df.info())

print('\ndescribe data')
print(df.describe())

print('\nmissing value')
check = df.isna().sum()
print(check)

print('check duplicate')
chk_d = df.duplicated().sum()
df.drop_duplicates(inplace= True)
check_d2= df.duplicated().sum()
print(check_d2)


df['category'] = df['category'].replace({'Bgas': 'Bags', 
                                         'Shoeses': 'Shoes', 
                                         'Clohting': 'Clothing'})

print(df.groupby('category')['price'].count())


print('\nadding missing value')

mean_price = df['price'].mean()
df['price']=df['price'].fillna(mean_price)

add_revenue = mean_price * 2
df['revenue']=df['revenue'].fillna(add_revenue)

mean_quant = df['quantity'].mean()
df['quantity'] = df['quantity'].fillna(mean_quant)

# check the null value again
check2 = df.isna().sum()
print(check2)


# check category of product along with their revenue 
x= df.groupby('category')['revenue'].sum().sort_index()
print(x)
plot the information 
sns.barplot(x , color= 'yellow')
plt.xticks(rotation= 45)
plt.xlabel('category')
plt.show()

# check which product is sell most 
check_most_sell_product = df.groupby('product')['quantity'].count().sum()
print(check_most_sell_product)

# plotting 
sns.countplot(x ='product',hue='category',data= df ,palette='rainbow')
plt.xticks(rotation = 60)
plt.show()
