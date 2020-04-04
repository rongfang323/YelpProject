#Business detail URL-- 'https://api.yelp.com/v3/businesses/{id}'
#Business reviews URL--'https://api.yelp.com/v3/businesses/{id}/reviews'

#Featured event URL -- 'https://api.yelp.com/v3/events/featured'
#Event search URL -- 'https://api.yelp.com/v3/events'
#Event look up URL -- 'https://api.yelp.com/v3/events/{id}'



import json
import pandas as pd



fileJson = 'business.json'
fileCSV = 'business.csv'
review_json= 'review.json'

#load json file
dat = []
headers = True
with open(fileJson, encoding="cp866") as f:
     for line in f:
         json_object =json.loads(line)
         dat.append(json_object)
         if headers:
             keys =[]
             #Read the Head of the datasets
             for k, v in json_object.items():
                 keys.append(k)

dat = pd.read_json(fileJson, lines=True)
# list all the categories of food/restaurant in Pittsburg, Phoenix and Charlotte
business_food = dat[dat['categories'].str.contains('Restaurant', case=False, na=False)]
city_food = business_food[business_food['city'].str.contains('Pittsburg|Phoenix|Charlotte', case = False, na = False)]




    #split the hour to individual keys




#Key words: Sandwiches, American (Traditional), American (New), Mexican, Pizza, Breakfast & Brunc, Burgers, Italian, Chinese, Japanese, Fast Food
#
#Style by country
df_explode = city_food.assign(categories = city_food.categories
                        .str.split(', ')).explode('categories')

print(df_explode.categories.value_counts()[:50])

df_filtered = df_explode[ (df_explode['categories'] != 'Restaurants') & (df_explode['categories'] != 'Food')
                       & (df_explode['categories'] != 'Nightlife') & (df_explode['categories'] != 'Bars')
                       & (df_explode['categories'] != 'Bars') & (df_explode['categories'] != 'Event Planning & Services ')
                       & (df_explode['categories'] != 'Caterers') & (df_explode['categories'] != 'Sports Bars')
                       & (df_explode['categories'] != 'Wine Bars') & (df_explode['categories'] != 'Pubs')
                       & (df_explode['categories'] != 'Arts & Entertainment') & (df_explode['categories'] != 'Juice Bars & Smoothies')
                       & (df_explode['categories'] != 'Ice Cream & Frozen Yogurt') & (df_explode['categories'] != 'Cocktail Bars')
                       & (df_explode['categories'] != 'Wine & Spirits') & (df_explode['categories'] != 'Food Delivery Services')]


print(df_filtered.categories.value_counts()[:50])
#Explore all type of categories
#df_explode = city_food.assign(categories = city_food.categories.str.split(', ')).explode('categories')
#Print the number of categories"""


size = 1000000
review = pd.read_json(review_json, lines = True, dtype = {"review_id": str,
                                                         'user_id': str,
                                                         'business_id': str,
                                                         'stars': int,
                                                         'date': str, 'text':str,
                                                         'useful': int, 'funny': int,
                                                         'cool': int}, chunksize = size)


#Join review file and business file by using business_id.
#The merge was performed as the unit of chunk.
chunk_list = []
for review_chunk in review:
    #rename colume name to avoid conflict with business overall star rating
    chunk_merged = pd.merge(df_filtered , review_chunk, on = 'business_id', how = 'inner')
    #show feedback on progress
    print(f"{chunk_merged.shape[0]} out of {size:,} related reviews")
    chunk_list.append(chunk_merged)
#concatenate all relevant data back to one dataframe
restaurant_review = pd.concat(chunk_list, ignore_index = True, join = 'outer', axis = 0)














