
# coding: utf-8

# In[423]:


# Scrapping works only for images from AIrbnb http://insideairbnb.com/get-the-data.html excel
import pandas as pd
import numpy as np
import urllib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time

#works in mac only and only for airbnb listings url 
#scrapped images from  the slide show for each airbnb listing
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
#https://twitter.com/search?q=%22YouTube%20HQ%22&src=tren&data_id=tweet%3A981284628614049794
data_url="https://twitter.com/hashtag/youtube%20hq?f=tweets&vertical=default&l=en"


# In[424]:


driver.get(data_url)
try:
    for i in range(1,200):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time_last=last.find_element_by_xpath("//small[@class='time']")
        time.sleep(2)

#time complexity in jupyter notebook
#    %timeit s = set(t)
    count=0   
    tweets_cont=driver.find_elements_by_xpath('//*[@id="stream-items-id"]/li')
    tweets_cont_set = list(tweets_cont)
    tweet=[];Account_Name=[];Account_id=[];Account_verified=[];tweet_datetime=[];
    Tweet_image=[];actions=[];
    for t in tweets_cont_set:
        count=count+1;
        print(count)
        try:
            a=t.find_element_by_class_name('js-tweet-text-container');
            b=t.find_element_by_class_name('stream-item-header');
            c=t.find_element_by_class_name('ProfileTweet-actionList');
            d=t.find_element_by_class_name('time').get_attribute('innerHTML');
#             d=t.find_element_by_xpath("//small[@class='time']")
            tweet.append(a.text)
#     tweet_datetime.append(d.split('title="')[1].split(' data-conversation-id')[0])
            tweet_datetime.append(d.split('title="')[1].split(' data-conversation-id')[0])
            user=[];actionList=[];
            user=b.text.split('\n')
            actionList=c.text.split('\n')
            actions.append(actionList)
#             Retweet.append(actionList[3])
#             Like.append(actionList[5])
            if(len(user)==5):
                Account_Name.append(user[0]);
                Account_id.append(user[2]);
                Account_verified.append("Yes")
            else:
                Account_Name.append(user[0]);
                Account_id.append(user[1]);
                Account_verified.append("No")
            count=count+1;
            try:
                e=t.find_element_by_class_name('AdaptiveMediaOuterContainer');
                botLink=e.find_element_by_tag_name('img');
                image=botLink.get_attribute("src")
                Tweet_image.append(image); 
            except:
                Tweet_image.append(" ");
                continue
        except:
            continue
            #print tweet.text
    df_list = pd.DataFrame({'tweet': tweet,
                            'Account Name':Account_Name,
                            'Account Id':Account_id,
                            'Account Verified':Account_verified,
                            'Actions':actions,
                            'Date Time':tweet_datetime,
                            'media':Tweet_image
                            
                            
                })
except NoSuchElementException:
    print data_url + "  is no longer available."
driver.close()


# In[426]:


df_list.to_csv("/Users/jaideep/Desktop/error_project/twitter_scrapped-2.csv", sep=',', encoding='utf-8')

