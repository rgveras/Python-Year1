"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 3

This file takes user inputs from main.py and implements them in functions
It includes a function that computes happiness scores by region and tweet, keyword tweets per region and total tweets per region

The average happiness value, number of keyword tweets and total tweets per region is returned as a tuple for each region

"""


def compute_tweets(tweet, keywords):

    def scores(tweets):                             # computes and returns happiness score of a tweet and a count value of 1 if a keyword is in the tweet
        count = 0
        sentVal = 0
        hapScore = 0
        for word in tweets:
            word = word.strip(PUNCTUATION).lower()
            if word in keydict:                     # checks if word is in 'keydict' dictionary (checks if its a keyword)
                count += 1
                sentVal += keydict[word]            # if the word is in the dictionary it adds its corresponding value toward the sentiment value sum
        if count != 0:
            hapScore = sentVal / count
            count = 1
        return hapScore, count

    keydict = {}
    keys = []                                       # a list that will become the keys in 'keydict'
    values = []                                     # a list that will become the corresponding values to the keys in 'keydict'
    PUNCTUATION = '[],.?/\'!@#;:\"{}'
    eastHapScore = 0
    centHapScore = 0
    mountHapScore = 0
    pacifHapScore = 0
    easternKeys = 0
    centralKeys = 0
    mountainKeys = 0
    pacificKeys = 0
    easternTweets = 0
    centralTweets = 0
    mountainTweets = 0
    pacificTweets = 0

    try:
        tweet = open(tweet, 'r', encoding='utf-8')
        keywords = open(keywords, 'r', encoding='utf-8')
    except IOError:
        return []                                   # returns empty list if file is not found

    for line in keywords:                           # adds the keys and values in each line to list 'key' and list 'value'
        keylist = line.strip().split(',')
        keys.append(keylist[0])
        values.append(keylist[1])

    for i in range(0, len(keys)):
        keydict[keys[i]] = int(values[i])           # sets the corresponding value to a key in the dictionary 'keydict'

    for line in tweet:
        tweetlist = line.split()                    # splits each line into separate words

        latitude = float(tweetlist[0].strip(PUNCTUATION))
        longitude = float(tweetlist[1].strip(PUNCTUATION))

        if 24.660845 < latitude < 49.189787 and -87.518395 < longitude < -67.444574:        # Eastern region
            easternTweets += 1
            eastHapScore += scores(tweetlist)[0]
            easternKeys += scores(tweetlist)[1]
        elif 24.660845 < latitude < 49.189787 and -101.998892 < longitude < -87.518395:     # Central region
            centralTweets += 1
            centHapScore += scores(tweetlist)[0]
            centralKeys += scores(tweetlist)[1]
        elif 24.660845 < latitude < 49.189787 and -115.236428 < longitude < -101.998892:    # Mountain region
            mountainTweets += 1
            mountHapScore += scores(tweetlist)[0]
            mountainKeys += scores(tweetlist)[1]
        elif 24.660845 < latitude < 49.189787 and -125.242264 < longitude < -115.236428:    # Pacific region
            pacificTweets += 1
            pacifHapScore += scores(tweetlist)[0]
            pacificKeys += scores(tweetlist)[1]

    easternAvg = eastHapScore / easternKeys
    centralAvg = centHapScore / centralKeys
    mountainAvg = mountHapScore / mountainKeys
    pacificAvg = pacifHapScore / pacificKeys

    eastern = easternAvg, easternKeys, easternTweets
    central = centralAvg, centralKeys, centralTweets
    mountain = mountainAvg, mountainKeys, mountainTweets
    pacific = pacificAvg, pacificKeys, pacificTweets

    regions = [eastern, central, mountain, pacific]

    tweet.close()
    keywords.close()

    return regions
