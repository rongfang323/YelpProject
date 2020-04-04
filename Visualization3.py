import matplotlib as plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

reviews = pd.read_csv('yelp_dataset/restaurant_review.csv')
reviews = reviews.sort_values(by = 'review_stars', ascending=True)
reviews  = reviews [(reviews ['city'] != 'Phoenix Valley') & (reviews ['city'] != 'East Pittsburgh')&
                        (reviews ['city'] != 'charlotte') & (reviews ['city'] != 'PHOENIX') ]


ax = sns.lmplot(x = 'funny', y = 'useful', hue = 'city', data = reviews)
ax.set(xlabel='Funny Votesllot', ylabel='Useful Votes')
plt.show()