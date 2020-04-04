import matplotlib as plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


reviews = pd.read_csv('yelp_dataset/restaurant_review.csv', dtype={'review_stars': str})
reviews = reviews.sort_values(by = 'review_stars', ascending=True)
reviews  = reviews [(reviews ['city'] != 'Phoenix Valley') & (reviews ['city'] != 'East Pittsburgh')&
                        (reviews ['city'] != 'charlotte') & (reviews ['city'] != 'PHOENIX') &(reviews['useful'] > 40)]



reviews_C = reviews[reviews['city'] == 'Charlotte']
reviews_P = reviews[reviews['city'] == 'Phoenix']
reviews_Pg = reviews[reviews['city'] == 'Pittsburgh']


ax = sns.boxplot(x="review_stars", y="useful", hue = 'city', data=reviews, palette="Set3")
ax.set(xlabel='Rating', ylabel='Useful Votes')
plt.show()

reviews_C.boxplot(column=['useful'], by = ['review_stars'])





