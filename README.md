# Capstone


Our Plan for the capstone project will proceed as follows:

DISCLAIMER: While this is what we currently plan on implementing, the project interpretation and deliverables are subject to change trying to deliver the maximum as per the assignment rubric 

Our plan is to implement a Stock market anakysis of sorts using previous year data as well as twitter sntiment anlysis to forecasst future stock market data

As it stands Chris and Shmail have been tasked to pull data as well as our data warehousing model in order to store our data so that it may be pulled later.

Data to be predicted using logistic reg:

   -close price

# systems and installs in use or planed fr production (add to list aswe move):
            Pthon
            pandas
            numpy
            tweepy
            ix_yahoo_finance
            scikit_learn
            maplotlib


# Machne Learning Model 

# model logic 
## Description of preliminary data
weve pulled the values for variables:
        open price
        close price
        volume traded 
        High

linear reg needs a forecast column to predict our close price - assume close price is our forecasted output 
if the basic formula of a linear reg. is as follows: y = B0 + B1*x1 + B2*x2 + m

our current machine learning algorithm takes previous years close data into account and then calculates a moving average over the course of 10 days as can be seen in our data cloum EMA_10 such that the first 10 days are represented by a NaN value. 


        
to predict the close price such that x1, x2 are the previous years close data and the moving average respectively
         - y is the close price that is to be predicted (i.e. future close price)
         - B is the constant term  
         - m is the error term 
        
## why did we choose linear reg?
linear reg was chosen as we have continuous tabulated data will be pulled, over the time frame for a year, a daily instance of every variable is expected to be present 

we may possibly adjust to a non linear reg upon seeing plotted data points 
     this may optimize our model to increase accuracy of predictibility 
        ADDITIONAL OPTIMIZATION: the addition or removal of terms to increase the accuracy of predictability 

## how will results be interpreted?
results will be interpreted using r^2 and adj. r^2 values to determine accuracy of prediction 

## why did we chose the associated variables? 
the associated variables are the most commonly talked about and used metrics when dealing with stock market data and predicting stock market data 
    furhter investigation will be done into more relavent variables that can be used but this will be a good base to launch off of 

## time window for prediction?
as we are using data consolidated from previous year it makes sense to predict movents of stock price either over the next yer from the date of query or till the end of the current year

## Feature engineering 
as a sentiment analysis is to be performed, that will be an additional term used in the linear reg. to increase the robustness of our predictions
the plan is to use sentiment analysis to determine the polarity of of tweets pulled using twitterDEV API such that we can created a weighted variable that will influence the final outcome of the prediction 


## Description of how data was split into training and testing sets ✓ Explanation of model choice, including limitations and benefits

Data was split in to training and testing sets at a ratio of 20%/80% to begin with this might be revisited after consulting with Ken

As Linear regression requires a series of assumptions to be made to be effective, an application of linear regeression not following the assumptions made would provide little to no insightful meanng

One of the assumptions is that variables in the data are independent, dictates that the residuals for any single variable aren’t related to the term being predicted.

As we are utilizing Time Series data this is often a problem since our observed values are longitudinal (i.e. they are observed values for the same thing, recorded in sequence). This produces a variable that is autocorrelated i.e. a variable that correlated to itslef. While this definitely has some insight under specific use cases, when it comes to extrapolating values for price prediction, however, it is problematic. Our date values aren’t suitable as our independent variable and we need to come up with something else and use the adjusted close value as the independent variable. 

In order to combath this issue, the exponential moving average was utilized but further more, a couple more indexes acan be used  to which we are researching into e.g. technical indicators such moving averages (SMA, MACD), the Relative Strength Index (RSI), Bollinger Bands (BBANDS)

-------------------------------------------------------------------------------------------------------
# Data Preprocessing 

will ned to perprocess data 
    split into X-train/test and Y-Train/Test where X-values will be OG close price? 
    cross valdiate sets 

apply linear reg algo to dataset and then plot using matpotlib to se results   
