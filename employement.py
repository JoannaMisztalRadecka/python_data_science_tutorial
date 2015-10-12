"""
Tutorial from:
https://www.dataquest.io/mission/113/challenge-summarizing-data/
Data from:
https://github.com/fivethirtyeight/data/tree/master/college-majors
"""

import pandas as pd
import matplotlib.pyplot as plt

# College majors and employment
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

# Summarizing major categories
all_ages_major_categories = dict()
recent_grads_major_categories = dict()
data_frames = [(all_ages, all_ages_major_categories), 
               (recent_grads, recent_grads_major_categories)]

for (df, df_dict) in data_frames:
    categories = df['Major_category'].value_counts().index
    for cat in categories:
        df_dict[cat] =  df[df['Major_category']==cat].sum()['Total']
		
#  Low wage jobs rates
low_wage_percent = float(recent_grads["Low_wage_jobs"].sum(axis=0)) / recent_grads["Employed"].sum(axis=0)
majors = recent_grads['Major'].value_counts().index

# Comparing datasets
recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0

majors = recent_grads['Major'].value_counts().index

recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0

for major in majors:
    recent_grads_major = recent_grads[recent_grads["Major"]==major]
    all_ages_major = all_ages[all_ages["Major"]==major]
    
    if recent_grads_major["Unemployment_rate"].iloc[0] < all_ages_major["Unemployment_rate"].iloc[0]:
        recent_grads_lower_emp_count+=1
    else:
        all_ages_lower_emp_count += 1
    
# data visualization
columns = ['Median','Sample_size']
recent_grads.hist(column=columns, layout=(2,1), grid=False)
#change bins number
recent_grads.hist(column=columns, bins=50)
#box plot 
recent_grads[['Total', 'Major_category']].boxplot(by='Major_category')
plt.xticks(rotation=90)
# multiple plots
plt.scatter(recent_grads["Unemployment_rate"], recent_grads["P25th"], color="red")    
plt.scatter(recent_grads["ShareWomen"], recent_grads["P25th"], color="blue")
plt.show()

        