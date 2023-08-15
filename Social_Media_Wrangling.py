import pandas as pd
import string

whitelist = '[^' + string.printable + ']' #Whitelist of printable characters

#FACEBOOK
facebook = pd.read_csv('facebook.csv')
facebook = facebook.drop(['title', 'in', 'hits', 'supports','images', 'url', 'byImageUrl'], axis = 1) #drop empty or useless columns
facebook = facebook.dropna() #drop 3 observations with NaNs
facebook['content'] = facebook['content'].str.replace(whitelist, ' ')
facebook.to_csv("facebook_cleaned.csv") #write finished data to csv

#TWITTER
twitter = pd.read_csv('twitter.csv')
twitter = twitter.drop(['title', 'images', 'url'], axis = 1) #drop unnecessary columns
twitter['content'] = twitter['content'].str.replace(whitelist, ' ')
twitter['by'] = twitter['by'].str.replace(whitelist, ' ')
twitter['from'] = twitter['from'].str.replace(whitelist, ' ')
twitter['locatiion'] = twitter['locatiion'].str.replace(whitelist, ' ')
twitter.to_csv("twitter_cleaned.csv") #write finished data to csv

#INSTAGRAM
instagram = pd.read_csv('instagram.csv')
instagram = instagram.drop(['title', 'images', 'url'], axis = 1) #drop empty or useless columns
instagram['content'] = instagram['content'].str.replace(whitelist, ' ')
instagram['from'] = instagram['from'].str.replace(whitelist, ' ')
instagram['location'] = instagram['location'].str.replace(whitelist, ' ')
instagram.to_csv("instagram_cleaned.csv") #write finished data to csv