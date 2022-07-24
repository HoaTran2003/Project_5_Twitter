# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 01:06:34 2022

@author: Hoa Tran 
FINAL PROJECT: SENTIMENT ANALYSIS
CS-112:DISCOVERING COMPUTER SCIENCE
HOA TRAN(JASON)
"""



##IMPORTING THE NECESSARY LIBRARIES:
import pandas as pd

import numpy as np
import re
import string
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
nltk.download('stopwords')
nltk.download('vader_lexicon')
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import ticker
import seaborn as sns
import plotly.express as px
from plotly.offline import plot

sns.set(style="darkgrid")


#Part 2: Plot the most common words
def plotmostcommon(text_cleaned): 
    '''
    

    Parameters
    ----------
    text_cleaned: DATA FRAME
        TWITTER TWEETS AFTER BEING POLISHED AND READY TO BE USED FOR ANALYSIS

    Return values
    -------
    None.

    '''
    words_list=[word for lines in text_cleaned for word in lines.split()] #finding the words and the lines in text and append them to a list
    
    
    
    #Finding the most common words:
    word_freq={}
    for i in words_list : #for loop to find the words frequency 
                  if i not in word_freq:
                      word_freq[i]=1
                  else:
                      word_freq[i]=word_freq[i]+1
    
    frequencyValues=list(word_freq.values()) #List of the values of in word_freq
    
    maxFrequency=max(frequencyValues) #finding the max value of the list
    mostFrequentKeys = [ ]
    
    for key in word_freq: #for loop to find check whether the max value above are correct or not
        if word_freq[key] == maxFrequency:
            mostFrequentKeys.append(key)
    
    
    sortedValues = [] # create list of (value, key) tuples
    
    for key in word_freq: #for loops to print out the most common words
        sortedValues.append((word_freq[key], key))
    sortedValues.sort(reverse = True) # sort in descending order
    print('{0:<20} {1}'.format('Key', 'Frequency'))
    print('{0:<20} {1}'.format('---', '---------'))
    for pair in sortedValues[:50]: # iterate over the sorted list
        key = pair[1]
        print('{0:<20} {1:>5}'.format(str(key), word_freq[key]))
    
    #Plot the most common words:
    word_counts=Counter(words_list).most_common(50) #using counter method to find the most common words 
    words_df=pd.DataFrame(word_counts) #create a data frame to the words frequency
    words_df.columns=["WORDS","FREQUENCY"] #name the two columns in the data frame
    
    fig=px.bar(words_df, x="WORDS",y="FREQUENCY",title="MOST COMMON WORDS") #plot the data frame with plotly library (because of interactive plots)
    plot(fig)
    
   

# Part 3: Sentimental analysis
def plotsentimental(text_cleaned,covid): 
    '''
    

    Parameters
    ----------
    text_cleaned : DATAFRAME
        TWITTER TWEETS AFTER BEING POLISHED AND READY TO BE USED FOR ANALYSIS
    covid : DATAFRAME
        THE DATAFRAME TAKEN FROM THE ORIGNAL DATASET CONSISTING OF THE COLUMNS: 
            DATES, TWEETS AND USER_NAME

    Returns values
    -------
    None.

    '''
   
    covid.text=text_cleaned #put the cleaned text into the main dataframe
    # Sentimental analysis:
    analyze=SentimentIntensityAnalyzer() #using the NPL toolkit to analyze (calling the analyser)
    ps_scores=lambda x : analyze.polarity_scores(x) #regular expression to analyze expression to analyze sentimental value by calculating the each tweet's polarity score
    sentiment_scores=covid.text.apply(ps_scores) #using a regular expression to apply the sentimental analysis to all of the tweets
    
    
    df_sentiment=pd.DataFrame(data=list(sentiment_scores)) #Put the sentimental scores into a seperate data frame
    
    labeling=[]
    for comp in df_sentiment['compound']:  #for loop used to label the sentiment value
        
        if comp==0: 
            labeling.append("Neutral")
        elif comp >0: 
            labeling.append("Postitive")
        else: 
            labeling.append("Negative")
    
    df_sentiment['label']=labeling
   
    
    plotdata=covid.join(df_sentiment.label) #join the label column to the main data frame

    #Plot the most common words:
    counts_label_df= plotdata.label.value_counts().reset_index() #count the number of neutral, postive and negative and reset the index of the resultant Python DataFrame
    sns.barplot(x="index", y="label", data=counts_label_df) #plot the most common words using bar graph 
    
    #Making a line plot of the changes in the sentminent of tweets over time:
    
    groupbydate=plotdata[['user_name', 'date', 'label']].groupby(['date','label']).count().reset_index()   #create a data frame with only the user_name, date and the label of the text and group them by text and label and then reset the indexes and also counting the number of labelling
    groupbydate.columns=['date','label','counts']  #change the column names  of user_name to counts
    
    fig2=px.line (groupbydate, x='date', y='counts', color='label', title='Analysis of sentimental value of daily tweets')#plot the sentimental value by dates and counts
    plot(fig2)
    
#Part 1: Cleaning the tweets and choosing data for analysis
def main(): 
    '''
    Parameters
    ----------
    None
   This function is used to clean the data and call the other functions above. 

    Return values
    -------
    None.
    '''
    
    #Importing the data set and clean the data: 
    covid=pd.read_csv("https://raw.githubusercontent.com/gabrielpreda/covid-19-tweets/master/covid19_tweets.csv") #using panda to load csv into data frame to seperate for easier analysis
    
    analyze_col=['user_name','date','text'] #select these columns for analysis
    covid=covid[analyze_col] # create a table of these columns 
    
    #Change the value types of the column for analysis
    covid.user_name=covid.user_name.astype("category") #change username into categorial data type
    covid.user_name=covid.user_name.cat.codes # using .cat.codes to assign a unique numerical value to each of the value in user_name column 
    covid.date=pd.to_datetime(covid.date).dt.date #change the date column to date time value using panda package
    
    #Picking out tweets text: 
    
    texts=covid['text']
  
    
  #Remove stop words, puncutations and http:// in the tweets
    
    for line1 in texts:  
        
        if "https://" in line1:
            
            line1=line1.replace("https://","") #for loops to delete the https:// in the tweets
            line1=line1.lower() #convert the tweets to lower case
            
    remove_puncs= lambda x: x.translate(str.maketrans('','',string.punctuation)) #remove the punctuations in the tweets
    
    texts=texts.apply(remove_puncs) #apply the remove puncutations to all of the tweets
    
    not_needed_words=["#COVID19","#coronavirus"," #Covid19","coronavirus19", "coronavirus","coronavirusoutbreak","coronavirusrusPandemic","coronaPandemic", "COVID19"] #some additional hashtagsto remove and not needed words (for better analysis)
    stop_words=set(stopwords.words("English")) #remove stop words (in English) that are in Tweets which arent necessary for sentimental analysis using the stopwords library in NPL toolkit
   
    stop_words.update(not_needed_words) #include the hashtags and uncessary words into the stopwords set
  
    remove_words=lambda x: ' ' .join([word for word in x.split() if word not in stop_words]) #using regular expressions and list comprehension to remove the stop words
    
    text_cleaned=texts.apply(remove_words) #apply the remove_words to the tweets to remove the stop words. 
    plotmostcommon(text_cleaned)
    plotsentimental(text_cleaned, covid)
main()
