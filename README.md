# YelpProject
This project creates three visuaulizations for restaurant business of Yelp open datasets. 
The open dataset is available on https://www.yelp.com/dataset/download
The detailed description is documented on https://www.yelp.com/dataset/documentation/main

two files were used for this project: business.json and review.json


#DataVisit.py
This file do some wrangling of the original business.json and review.json file. 
The process filts the desirable restaurant categories and join business.json and review.json by the business_id field.

#Visualization
This file creates plots for the ten most popular restaurant categories for cities of Pittsburg, Phoenix, and Charlotte and their average reviews.

#Visualization2
This file creates a side-by-side boxplot for the number of vetos as 'useful' by the rating and cities.

#Visualization3
This file creates a scatterplot of number of votes as 'useful' vs. number of votes as 'funny'.

#Result Explanation
This document explains the results obtained from the visualization. 
