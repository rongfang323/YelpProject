import matplotlib as plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

city_food = pd.read_csv('yelp_dataset/popCat_city.csv')
city_food = city_food.sort_values(by = 'count', ascending=False)
city_food_C = city_food[city_food['city'] == 'Charlotte']
city_food_P = city_food[city_food['city'] == 'Phoenix']
city_food_Pg = city_food[city_food['city'] == 'Pittsburgh']
print(city_food)

fig, ax = plt.subplots(ncols = 3, nrows= 1)
ax[0].bar(city_food_C['categories'], city_food_C['count'])
ax[0].set_xticklabels(city_food_C['categories'], rotation=45, ha='right', size = 8)
ax[0].set_ylim([0, 800])
ax[0].set_title("Charlotte")
ax[0].set_ylabel("Count")
ax2 = ax[0].twinx()
ax2.set_ylim([2.5, 3.8])
ax2.plot(ax[0].get_xticks(),city_food_C['rating'], linestyle='-', marker='o', color = 'darkorange')
ax2.yaxis.set_visible(False)


ax[1].bar(city_food_P['categories'], city_food_P['count'])
ax[1].set_xticklabels(city_food_P['categories'], rotation=45, ha='right', size = 8)
ax[1].set_ylim([0, 800])
ax[1].set_title("Phoenix")
ax[1].yaxis.set_visible(False)
ax2_1 = ax[1].twinx()
ax2_1.set_ylim([2.5, 3.8])
ax2_1.plot(ax[1].get_xticks(),city_food_P['rating'], linestyle='-', marker='o', color = 'darkorange')
ax2_1.yaxis.set_visible(False)


ax[2].bar(city_food_Pg['categories'], city_food_Pg['count'])
ax[2].set_xticklabels(city_food_Pg['categories'], rotation=45, ha='right', size = 8)
ax[2].set_ylim([0, 800])
ax[2].set_title("Pittsburgh")
ax[2].yaxis.set_visible(False)
ax2_2 = ax[2].twinx()
ax2_2.set_ylim([2.5, 3.8])
ax2_2.plot(ax[2].get_xticks(),city_food_Pg['rating'], linestyle='-', marker='o', color = 'darkorange')
ax2_2.set_ylabel("Average rating")

plt.gcf().subplots_adjust(bottom=0.25)
plt.show()


