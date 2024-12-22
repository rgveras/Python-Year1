"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 3

This file accesses the function compute_tweets from the file sentiment_analysis.py
It is returned the average happiness value of each region, the number of keyword tweets and the total number of tweets

It then prints the values of each, with the happiness value to 4 decimals, in a tabular presentation

"""

from sentiment_analysis import compute_tweets

keywordFile = input('Enter the file containing the keywords: ')
tweetFile = input('Enter the file containing the tweets: ')

tweetResults = compute_tweets(tweetFile, keywordFile)               # assigns returned values of compute_tweets to 'tweetResults'

print('%20s %20s %20s %20s' % ('', 'Average Happiness', 'Keyword Count', 'Total Tweet Count'))

regions = ['Eastern', 'Central', 'Mountain', 'Pacific']
count = 0

for region in tweetResults:                                                 # prints the values of each region in tweetResults in a table
    print('%20s %20.4f %20d %20d' % (regions[count], region[0], region[1], region[2]))
    count += 1                            # this line counts to iterate through the list 'regions' in the previous line

