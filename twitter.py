from TwitterSearch import *
import json
import numpy as np
import pandas as pd
import datetime
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['ParklandShooting', 'florida','school']) # let's define all words we would like to have a look for
    #print(datetime.datetime.strptime('20180215', "%Y%m%d").date())
    
    tso.set_language('en') # we want to see German tweets only
    #tso.set_until(datetime.date(2018, 02, 24))
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create TwitterSearch object again
    ts = TwitterSearch(
        consumer_key = '2Ukxf5ebLxYRo6KDM1H1X7jJp',
        consumer_secret = 'YNiVdrlG4AxnbZIOLSeUy3AuHhS1Bfg22ruykeEOqxQ6t6kUZ9',
        access_token = '90850783-ji9l9FE1KqarK2KsZzt4G3tVEO1dVt77QPi20BSu8',
        access_token_secret = '9vtJIZjOZIRKJCHGAedlJcA0swB2G8DxwNfbGexcdBpVv'
    )

    # start asking Twitter about the timeline
    txt=[];retw=[];crea=[];loc=[]
    for tweet in ts.search_tweets_iterable(tso):
         txt.append(json.dumps(tweet['text']))
         retw.append(json.dumps(tweet['retweet_count']))
         crea.append(json.dumps(tweet['created_at']))
         loc.append(json.dumps(tweet['user']['location']))
    df_list = pd.DataFrame(
                           {'txt':txt,
                           'retweet':retw,
                           'created_tweet':crea,
                           'location':loc
                           }
                        )
    df_list.to_csv("twitter.csv",sep=",")

except TwitterSearchException as e: # catch all those ugly errors
    print(e)
