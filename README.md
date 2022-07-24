# Project_5_Twitter

SENTIMENT ANALYSIS

I.	INTRODUCTION 

With the rapid changes of the Covid-19 pandemic, people’s perspective of it has always been drastically different. Most notably, such a drastic difference can be seen on many social media platforms such as Twitter and Facebook. Because of this, analysis of the sentiment value of social media , especially Twitter’s tweets, will be of crucial importance in understanding how the public is viewing the pandemic. 

II.	Algorithm explanation: 

This project focuses on primarily on the analysis of Twitter’s tweets. In order to do so, I divide the project into three main parts utilizing Python’s built in text analysis librar: NPL toolkit

Part 1: Cleaning the tweets 
In order to do this part, I need to clean the tweets first as there are unesscary parts in them which make the analysis inaccurate or maybe misleading. First of all, in some Tweets, there are links to lots of websites which are unneeded for analysis as they contain no sentiment value. Therefore, I have to remove the :https://” in the links.  Moreover, there are lots of stop words (words that need to be filtered out so that the NPL toolkit can analyze accurately the sentiment value). The puncuations in the tweets are also needed to be filtered out due to the fact that analysis of them will bring no useful results. As for the convenience of using the NPL toolkit, I will also need to turn all of the letters in the tweets to lowercase letters. 

Part 2: Finding the most common words: 
After having cleaned the tweets, I need to find the most common words (in this project, I have narrowed it down to 50). This is because knowing the frequency of words can help me to formulate some research questions regarding how positive and negative are people’s perspective of the pandemic 

Part 3: Sentiment analysis: 
In this part, after having found the most common words, the next step is to analyze the sentiment value of the polished text. To do this, after having used the NPL toolkit to analyze the text, instead of displaying the scores for each tweet, I decide to show the number of positive, negative and neutral tweets. After that, displaying how the number of such tweets change throught the surveyed period is necessary to see how people’s sentiment also change. 

III.	Algorithm implementation: 
The project has three functions: main(), plotmostcommon() and plotsentiment(). 

The main() function is where the program begins. This function takes no parameters. In this function, the tweets are imported from a link and are read as csv format using panda library. After that, I choose the necessary columns for analysis which are user_name, date and text. Next, I convert the type of the user_name to categorical and assign each user_name with a unique numerical value by using . For the date column, I change the format to date time value (month/date/year)for better analysis instead of putting it in hours format (for the purpose of making a line plot). Then, a for loop is created to delete the “https://” in tweets and also to convert all of the tweets to lower case letters. Moreover, I also make a translation table through regular expressions to remove the punctuations in the tweets. The reason for this is because of memory efficiency as I have tried using for loops and lists to do this but I encounter memory error. Next, I use the stop words package built in the NPL toolkit to remove the stop words and I aslo add other unnecessary words to the set of stop words. After that, I use regular expression to apply the remove stop words to all of the tweets to remove them.

The plotmostcommon() function takes the text_cleaned(a data frame containing all of the tweets) as a parameter. In this function, a word list was created to store all of the words in the tweets and split them apart. After that, a dictionary was created to store the words as keys and their frequencies as values. Next, a for loop was used to count the words frequencies in the list above. Moreover, another for loop was used to validate the correctness of the for loop used to count words frequencies. Another for loop is also used to print out the most common words( for this project I chose 50). Then, to plot the most common words (validation of the print results) I use the counter method to find the 50 most frequent words in word_lists. Then I create a data frame containing the most frequent words and named the two columns in it as “WORDS” and “FREQUENCY”. Finally, a bar chart was made by using the data frame above to display the words frequency. 

The plotsentiment() function takes text_cleaned and covid as parameters, both of which are dataframes. The main goal of this function is to plot the sentiment value of the text using a line plot(showing changes throughout the surveyed period) and the count of positive, negative and neutral texts. To do so, first, the sentimental analysis packaged was used to analyze the entire tweets using regular expressions and built in method in NLTK library. Next, the sentimental scores are put into a list and the list was convered into a dataframe in panda. Then, a for loop was created to change the labeling of each tweet based on the polarity scores. After that, the labeling column created in the for loop was joined in the main dataframe. A bar plot showing the counts of positive and negative as well as neutral tweets were created using the dataframe above. Following this, a new dataframe was created by using the data frame above (main dataframe joined by the labeling column) by choosing only “user_name”, “date” and “text” column and grouping everything by “date” and “label”. The three columns in the dataframe was then named as “date”, “label” and “count”. Finally, a line plot using this dataframe was created to show the changes in the number of positive and negative as well as neutral tweets in the time span of analysis. 

IV.	Results and findings: 


 
Key                  Frequency
---                  ---------
cases                16286
The                  15146
I                    13198
Covid19              12841
amp                  11903
new                  10703
covid19               8958
people                8037
pandemic              6164
deaths                6033
We                    5533
This                  5019
A                     4703
Coronavirus     4394
positive              4156
In                    4060
one                   3835
2020                  3830
India                 3822
like                  3735
us                    3702
New                   3609
get                   3556
If                    3529
realDonaldTrump       3519
US                    3439
today                 3351
need                  3197
health                3116
mask                  3115
COVID19…              3107
How                   3106
time                  3069
last                  2983
help                  2906
vaccine               2872
day                   2849
reported              2818
August                2807
know                  2802
Trump                 2758
many                  2755
spread                2596
What                  2592
As                    2591
You                   2510
due                   2494
total                 2453
number                2447
2                     2435

The following results and graphs show the 50 most common words in the tweets. Some of the most noticeable words are “cases”, “death”, “people”, “positive”, “pandemic”. This indicates that people were discussing a lot more about the pandemic (information related to cases, death rate and postive cases), suggesting that some of the tweets have negative tone to them. Moreover, there are more words such as “Trump”, “realDonalTrump” as well as “India”, showing that during the time of this pandemic, there were lots of discussions related to the situation in India as well as related to the US presidents of the time. Overall, most of the tweets seem to be slightly negative but still bear some positive perspective in them. With this assumption, I decided to count the number of positive and negative tweets and then showing their changes to validate my hypothesis. 

#Number of positive, negative and neutral tweets:
 

The bar chart above shows that the majority of the tweets (nearly 70,000) are positive while nearly 60,000 of them are negative. The remaining tweets are neutral in their sentimental value. This contradicts with my hypothesis as there are a lot more positive tweets compared to negative ones. This means that people’s discussions may contain negative words but the overall sentiment value of their tweets are actually positive. Because of this, my initial assumption was disproved as shown in the graph above.

 

The bar chart displays the changes of count of the sentiment of daily Tweets throughout the surveyed period with major fluctuations. Overall, there seemed to be less tweets about Covid-19 and the count for each sentinment value (neutral, negative or positive) seemed to be decreasing. This could be explained by the constant changing state of the pandemic. Noticeably, there are major dips (decreases) between July and August as well as in around the time of Augsut 9th and then the lines spiked up shortly afterwards. This feature clearly showcased the elasticity in the changes of people’s perspective during Covid-19 as only in a few hours, sentiment value counts could change so drastically. 

VI.	Conclusion: 

Overall, in the time span of my analysis, people’s sentiment towards the pandemic was slightly optimistic with the most common words being:
. However, there were constant fluctuations in the sentiment value throughout the surveyed period, showing that with the constant changes in the state of the pandemic, people’s sentiment also follow said changes. 
All of this clearly shows that people’s sentiment to the pandemic are actually relatively elastic in accordance with the state of Coivd-19. 
