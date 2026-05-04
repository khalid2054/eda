import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\practice\netflix_titles.csv")
# # print(df)

# # # check the upper 10 line of data 
print(df.head(10))

# # # check the sahpe of data 
print(df.shape)

# # # see all columns
chech_column = df.columns.to_list()
print(chech_column)
    
# # # get info of data
df.info()
    
# # # check null value
check1 = df.isna().sum()

# # #  fill the  missing data
val = {'director' : 'unknown' ,  'cast' : 'null' , 'country' : 'not-defined'}
df.fillna(value=val , inplace= True)

# # # drop rows 
df.dropna(subset=['date_added','rating' , 'duration'], inplace= True)

# # check agian null value
check2= df.isna().sum()
print(check2)



# .....1
# check the difference in tv show or movie
print(df['type'].value_counts())
# # # plot of wacthing type
sns.countplot(data= df , x= 'type')
plt.title('category')
plt.xlabel('category name')
plt.ylabel('counts..')
plt.show()
# Movies (6k+) are nearly 2x more than TV Shows (3k),
# indicating Netflix heavily focuses on movie content"


# # check the country ratio 
print(df['country'].head(10))
x  = df['country'].value_counts().head(10)
# # # plot of country ratio
plt.figure(figsize=(10,6)) 
sns.barplot(x)
plt.title('country ratio', loc='center')
plt.xlabel('countries name')
plt.ylabel('production')
plt.tight_layout()
plt.show()
#  Movies from Usa is more than +2.5k which make USA largest production house,
# after USA india stand for second place with more then 1000 movie  
# least it mexico with aprrox 90-100 movie 



# # # # top rating
rating_data = df['rating'].value_counts().head(10)
print(rating_data)
# # # plot of rating bar
sns.barplot(rating_data,color= 'yellow',)
plt.title('top rating',loc='center')
plt.tight_layout()
plt.show()
# "TV-MA dominates with 3200+ titles, followed by TV-14 at ~2200,
# indicating Netflix primarily targets mature audiences (18+)"



# # # # check release year 
year_data= df['release_year'].value_counts().sort_index().tail(10)
print(year_data)
# # #  make plot of year data
sns.barplot(year_data, color= 'grey')
plt.title('YEAR-WISE DATA')
plt.xlabel('years')
plt.tight_layout()
plt.show()
# "Content grew steadily from 2012, peaked in 2018 at ~1150 titles, 
# then slightly declined — likely due to COVID impact on production in 2020-2021"


# # # # data for director 
filter_director = df[(df['director'] != 'unknown' )]
director_data = filter_director['director'].value_counts().head(10)
print(director_data)
# # # plot for director analysis
plt.figure(figsize=(12,8))
sns.barplot(director_data, color= 'green')
plt.xticks(rotation = 45, ha = 'right')
plt.title('Analysis for director')
plt.tight_layout()
plt.show()
# "Rajiv Chilaka leads with 19 titles, mostly children's content. 
# Top directors have 11-19 titles each,
# showing no single director heavily dominates the platform"




# # analysis of genra
print(df['listed_in'].head(50))
split_data= df['listed_in'].str.split(',')
genra_data = split_data.explode().str.strip().value_counts().head(10)
# # plot of genra data
sns.barplot(genra_data, color='blue')
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()
# "International Movies top at 2700+, followed by Dramas and
# Comedies — showing Netflix has strong global 
# and entertainment-focused content strategy"