import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns

# read csv and create a Pandas dataframe
df = pd.read_csv('athlete_events.csv')

# let's see the headers
print(df.columns)

# there are repetitive rows in the dataset. We need to remove these
# to obtain correct values. So, remove duplicates.
df.drop_duplicates()


# let's count male and female athletes for each olympic year, and
# add as a new column to our dataframe
result = DataFrame({'Count' : df.groupby(["Year", "Sex"] ).size()}).reset_index()


# dataset consists of years from 1896 to 2016,
# and there are inconsistency between 1992 and 2016
# so, I removed the data of 1996 and later
result= result[result.Year < 1993]


# this is where data visualization starts!
# firstly, import seaborn
sns.set_theme(style="whitegrid", palette=None)

emre = sns.catplot(x="Year",       # x variable name
            y="Count",       # y variable name
            hue="Sex",  # group variable name
            data=result,     # dataframe to plot
            kind="point",   # graph type
            # linestyles=["-", "--"], redundant
            # markers=["^", "o"], redundant
            ci="sd")

emre.set_axis_labels("", "")  # redundant because title explains axises

# For Title
plt.title('Number of Male(M) and Female(F) olympic athletes between 1896-1992', weight='bold')
# For Subtitle
plt.text(x=2, y=11000, s='Global political and economical tensions have affected sport '
                         'organizations such as olympic games. The world wars\n'
                         'caused eight and twelve years gaps respectively. While no interruption in '
                         'the games since 1948, unbalance situation\n'
                         'of male-female athlete numbers has continued.', fontsize=10,)

plt.show()
