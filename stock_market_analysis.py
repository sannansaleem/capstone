#Stock market anakysis using previous year data as well as twitter sntiment anlysis to predict htisyears stock market data
    #Data to be predicted using logistic reg:
        #open price
        #close price
        #volume traded
        #High
        #low

#systems and installs in use or planed fr production (add to list aswe move):
            #Pthon
            #pandas
            #numpy
            #tweepy
            #ix_yahoo_finance
            #scikit_learn
            #maplotlib


#Code ideas start 

#create data frame that contines all stock ticker indexes 
    #indexes will be used t ask user for a prompt 'wich ticker  data would youike to pull' 
        #data that uesr enters has to be referenced with the created dataframe to makesure the tcker entered by the user actuall exists 
#challenges posed:
    #where are we puing this data frm? can we use fix_yahoo_finace 

#-----------------------------------------------------------------------------------------------------

#Create Dataframe containing stock data using value that user enters 
#pulls todays dte
actual = dt.date.today()
#subtrats 365 days from the pulled date to fnd prev date makign it a years time frame. Can we increase the data pulled for reater robusness i.e 2+ years???
past = actual - dt.timedelta(days=365)

#pull data fr the ticker in question using fix_yahoo_finance  how do we call on the uesr entered info? store it in a variable?
data = yf.download("<insert ticker index here>", start=past, end=actual)
#build datafme of stock data 
df = pd.DataFrame(data=data)

#-------------------------------------------------------------------------------------------------------
#Modelling behviour 

#model logic 
#weve pulled the values for variables:
        #open price
        #close price
        #volume traded 
        #High

#linear reg needs a forecast column to predict our close price - assume close   price is our forecasted output 
# if the basic formula of a linear reg. is as follows: y = B0 + B1*x1 + B2*x2 + B3*x3 + m
    #we plan to implement a ML algo that takes :
        #open price
        #close price
        #volume traded 
        #High
    # to predict the close price such that x1, x2, x3, x4 are the pulled variables
        # y is the close price that is to be predicted (i.e. future close price)
        # B is the constant term  
        # m is the error term 
        
#linear reg needs a forecast column to predict our close price - assume close   price is our forecasted output 

#-------------------------------------------------------------------------------------------------------
#Data Preprocessing 
#will ned to perprocess data 
    #split into X-train/test and Y-Train/Test where X-values will be OG close price? 
    #cross valdiate sets 

#apply linear reg algo to dataset and then plot using matpotlib to se results   

#-------------------------------------------------------------------------------------------------------

#twitter senitment anlysis 
    #use twitterDEV to retrieve the last 'x' amount o tweets containing the ticker index taken from uesr
        #are we able to recall var reated   initially to store the index 
                #check config.py file 
    # need to conduc sentiment analsis, what API can we use to deermine and quantify the polarity of a tweet.
    


