# EDA ....1


# step ....1
import seaborn as sns 
import matplotlib.pyplot as  plt
df = sns.load_dataset('titanic')
print(df)

# headline..
print('Headlines..')
print(df.head(10))

# shape...
print('Shape of data...')
print(df.shape)

print('Info of data....')
print(df.info())

# check the null value in data
print(df.isna().sum())

# drop unwanted column
df.drop(['deck', 'alive' , 'embarked','embark_town','who', 'class','adult_male', ] ,axis= 1 ,inplace = True)
print(df)

# fill missing value 
mid_age = df['age'].median()
print(mid_age)
df['age'].fillna(mid_age,inplace=True)

# check again after filling missing data
print(df.isna().sum())


# step.....2 
#  Univariate Analysis.
print('check survival count')
print(df['survived'].value_counts())

print('check sex count')
print(df['sex'].value_counts())

print('check survive rate in between menor women')
print(df.groupby('sex')['survived'].mean())

print('check suvival rate in betweem classes')
print(df.groupby('pclass')['survived'].mean())

print('check age column for get detail info of age difference in ship')
print(df['age'].describe())

print('check fare')
print(df['fare'].describe())


# step 3 .........
# chart for to check survival ratio 
sns.countplot(x ='survived' , data= df)
plt.show()

sns.countplot(x = 'sex' ,hue = 'survived',data = df)
plt.show()


sns.plot(x = 'pclass' ,hue = 'survived',data = df)
plt.show()