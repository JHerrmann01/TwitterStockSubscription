
import json
import requests
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import time
from yahoofinancials import YahooFinancials

from twython import Twython, TwythonError
import dateparser
import sqlite3
import twitter







symbolArray = ["MSFT", "AAPL", "GOOGL", "GOOG", "FB", "INTC", "CSCO", "ORCL", "SAP", "ADBE", "IBM", "CRM", "AVGO", "TXN", "NVDA", "VMW", "ADP", "QCOM", "INTU", "ITW", "BIDU", "MU",
		"INFY", "CTSH", "NOW", "WDAY", "AABA", "DELL", "AMAT", "HPQ", "NOK", "ADSK", "ETN", 
		"ATVI", "FISV", "EA", "RHT", "SQ", "XLNX", "LRCX", "NXPI", "WIT", "TEAM", "AMD", "TWTR",
		"MSI", "HPE", "MCHP", "AMZN"]
	
stockNameArray = ["Microsoft", "Apple", "Alphabet", "Alphabet", "Facebook", 
		    "Intel", "Cisco Systems, Inc.", "Oracle", "SAP SE", "Adobe", "IBM", 
		    "Salesforce", "Broadcom", "Texas Instruments Incorporated", "NVIDIA", 
		    "Vmware", "ADP", "QUALCOMM", "Intuit", 
		    "Illinois Tool Works Inc.", "Baidu", "Micron Technology", "Infosys Limited", 
		    "Cognizant Technology Solutions Corporation", "ServiceNow", "Workday", "Altaba",
		    "Dell", "Applied Materials", "HP", 
		    "Nokia", "Autodesk", "Eaton", "Activision", 
		    "Fiserv", "EA", "Red Hat", "Square", "Xilinx", 
		    "Lam Research Corporation", "NXP Semiconductors N.V.", "Wipro Limited", "Atlassian Corporation Plc", 
		    "Advanced Micro Devices, Inc.", "Twitter, Inc.", "Motorola Solutions", 
		    "Hewlett Packard Enterprise Company", "Microchip Technology Incorporated", "Amazon"]

NEWS_ARTICLE_API_KEY = "849198c20dc146dabe5508281d0912f7";
NEWS_ARTICLE_ENDPOINT = "https://newsapi.org/v2/top-headlines" + "?apiKey=" + NEWS_ARTICLE_API_KEY + "&sortBy=popularity" + "&language=en" + "&q=";

twitterAPI = None
twitterAPIForDM = None
googleAPI = None





    




'''DATABASE STUFF'''
DATABASE_URL = "/home/jeremy/Desktop/TwitterStockSubscription/UserStockDB"
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Query will be used to get information from the database #
def query_db_target(query, database, args=(), dictionary = True):
    con = sqlite3.connect(database)
    if dictionary:
        con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.commit()
    con.close()
    return rv

# Post will be used to change/input information into the database #
def post_db_target(query, database, args=()):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(query, args)
    con.commit()
    con.close()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def initTwitterAPI():
    global twitterAPI
    global twitterAPIForDM
    consumer_key = 'm5F6xGgDXeC8fP7HYyb0gsu0Q'
    consumer_secret = 'AHTRDLn7QxYYnIZKA3oeDllruKKcQRLAQrtRxD5T6bEI0nvK77'
    access_token = '907456144297295872-l3ui8Q50p7wcLZvkZuinV7Ju14GBrxH'
    access_token_secret = 'tSQGmqIli4wa9gZxvpPfh7irWRUf5BAPMh7TuvmWHu6z9'

    twitterAPI = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    twitterAPIForDM = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_token, access_token_secret=access_token_secret)

def initGoogleAPI():
    global googleAPI
    # Setting environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/jeremy/Desktop/TwitterStockSubscription/studious-metric-231904-9ac90bc14eb9.json"
    # Instantiates a client
    googleAPI = language.LanguageServiceClient()

def postToTwitter(Message):
    global twitterAPI
    twitterAPI.update_status(status=Message)


def getNewsArticles(Company):
    currentEndpoint = NEWS_ARTICLE_ENDPOINT + Company
    response = requests.get(currentEndpoint)
    response = json.loads(response.text)
    if(int(response['totalResults']) == 0):
        return([])
    return(response['articles'])

def analyzeArticle(Text):
    global googleAPI
    if(Text == None):
        return([0, 0])
    #text = u'Hello, world!'
    document = types.Document(
        content=Text.encode('utf-8').decode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = googleAPI.analyze_sentiment(document=document).document_sentiment
    time.sleep(0)

    return([sentiment.score, sentiment.magnitude])

def getCurrentData(CompanyList):
    result = []
    for x in range(0, len(CompanyList)):
    #for x in range(0, 2):
        print("Working on: " + CompanyList[x])

        #Getting the current stock price
        stockPrice = YahooFinancials(CompanyList[x]).get_current_price()

        companyName = stockNameArray[symbolArray.index(CompanyList[x])]

        #Getting all recent articles about the current stock
        articles = getNewsArticles(companyName)

        currentVolatility = 0
        articleInfoList = []
        for article in articles:
            print(article['title'])
            tempArticleInfo = []

            articleAnalysis = analyzeArticle(article['description'])
            print("The output from the article: " + str(articleAnalysis)) 
            #ArticleAnalysis[0] --> Sentiment Value ( Is the statement positive or negative ) [ -1, 1]
            #ArticleAnalysis[1] --> Sentiment Magnitude (How positive or negative a statement is ) [0, +inf)
            currentVolatility += articleAnalysis[0] * articleAnalysis[1]
            tempArticleInfo.append(article)
            tempArticleInfo.append(articleAnalysis)
            articleInfoList.append(tempArticleInfo)
        
        
        tempData = [CompanyList[x], companyName, articleInfoList, currentVolatility, stockPrice]
        print("Current Data: ")
        print("Stock Symbol - " + tempData[0])
        print("Stock Name   - " + tempData[1])
        print("Current Stock Price - " + str(tempData[4]))
        print("Articles & Information: ")
        for articleInfo in tempData[2]:
            print(articleInfo[0]['title'])
            print(articleInfo[1])
            print()
        print("Volatility: " + str(tempData[3]))
        print("Done with this stock!")
        print("\n\n\n")
        
        result.append(tempData)
    return(result)

def updateDatabaseOfUserStockFollowing():
    global twitterAPI
    if(twitterAPI == None):
        initTwitterAPI()

    TWITTER_ACCOUNT_NAME = "Zap173"

    #Getting previous messages
    previousMessages = twitterAPI.get_direct_messages()

    #Traversing the list of messages
    for message in reversed(previousMessages):
        #Checking if the message was received vs sent by our BOT        
        if(message["recipient_screen_name"] == TWITTER_ACCOUNT_NAME):
            print(json.dumps(message['text'], indent=4, sort_keys=True))

            senderUsername = message["sender"]["screen_name"]
            senderUserID = message["sender_id"]
            messageContent = message["text"]
            messageId = message["id"]

            if(messageContent.split(" ")[0] == "Follow"):
                if(messageContent.split(" ")[1] not in symbolArray):
                    continue
                #If there is a row in the DB with the same messageID, then alreadyExists will be set to 1, else 0
                alreadyUsedMessage = (query_db_target("SELECT COUNT(1) FROM `tTwitterMessages` WHERE `messageId`=" + str(messageId) + ";", DATABASE_URL)[0]['COUNT(1)'] == 1)
                if(not alreadyUsedMessage):
                    userExists = (query_db_target("SELECT COUNT(1) FROM `tUsers` WHERE `userId`=" + str(senderUserID) + ";", DATABASE_URL)[0]['COUNT(1)'] == 1)
                    if(not userExists):
                        post_db_target("INSERT INTO `tUsers` (userId, username) VALUES(?, ?)", DATABASE_URL, (senderUserID, senderUsername))
                    stockExists = (query_db_target("SELECT COUNT(1) FROM `tStock` WHERE `stockSymbol`='" + str(messageContent.split(" ")[1]) + "' AND `stockname`='" + str(stockNameArray[symbolArray.index(str(messageContent.split(" ")[1]))]) + "';", DATABASE_URL)[0]['COUNT(1)'] == 1)
                    if(not stockExists):
                        post_db_target("INSERT INTO `tStock` (stockSymbol, stockname) VALUES(?, ?)", DATABASE_URL, (str(messageContent.split(" ")[1]), str(stockNameArray[symbolArray.index(str(messageContent.split(" ")[1]))])))
                    relationshipExists = (query_db_target("SELECT COUNT(1) FROM `tStockUserRelation` WHERE `stockSymbol`='" + str(messageContent.split(" ")[1]) + "' AND `userId`=" + str(senderUserID) + ";", DATABASE_URL)[0]['COUNT(1)'] == 1)
                    if(not relationshipExists):
                        post_db_target("INSERT INTO `tStockUserRelation` (stockSymbol, userId) VALUES(?, ?)", DATABASE_URL, (str(messageContent.split(" ")[1]), senderUserID))

                    post_db_target("INSERT INTO `tTwitterMessages` (messageId, content, senderId, receiverId) VALUES(?, ?, ?, ?)", DATABASE_URL, (str(messageId), str(messageContent), str(senderUserID), TWITTER_ACCOUNT_NAME))
            elif(messageContent.split(" ")[0] == "Unfollow"):
                if(messageContent.split(" ")[1] not in symbolArray):
                    continue
                
                #If there is a row in the DB with the same messageID, then alreadyExists will be set to 1, else 0
                alreadyUsedMessage = (query_db_target("SELECT COUNT(1) FROM `tTwitterMessages` WHERE `messageId`=" + str(messageId) + ";", DATABASE_URL)[0]['COUNT(1)'] == 1)
                if(not alreadyUsedMessage):
                    relationshipExists = (query_db_target("SELECT COUNT(1) FROM `tStockUserRelation` WHERE `stockSymbol`='" + str(messageContent.split(" ")[1]) + "' AND `userId`=" + str(senderUserID) + ";", DATABASE_URL)[0]['COUNT(1)'] == 1)
                    if(relationshipExists):
                        post_db_target("DELETE FROM `tStockUserRelation` WHERE `stockSymbol`='" + str(messageContent.split(" ")[1]) + "' AND `userId`=" + str(senderUserID) + ";", DATABASE_URL)

                    post_db_target("INSERT INTO `tTwitterMessages` (messageId, content, senderId, receiverId) VALUES(?, ?, ?, ?)", DATABASE_URL, (str(messageId), str(messageContent), str(senderUserID), TWITTER_ACCOUNT_NAME))
            else:
                continue

def sendDirectMessage(userId, message):
    global twitterAPIForDM
    twitterAPIForDM.PostDirectMessage(message, user_id=userId)

def sendDailyDirectMessage():
    #Updating the DATABASE based on the recent DMs
    updateDatabaseOfUserStockFollowing()
    
    #Query for all the stocks we need to get information for
    requestedStocks = query_db_target("SELECT GROUP_CONCAT(`stockSymbol`) FROM `tStockUserRelation`;", DATABASE_URL)[0]["GROUP_CONCAT(`stockSymbol`)"]
    if(requestedStocks is None):
        requestedStocks = []
    else:
        requestedStocks = requestedStocks.split(",")

    currentData = getCurrentData(requestedStocks)
    #print(currentData)
    
    allRelations = query_db_target("SELECT `userId`, GROUP_CONCAT(`stockSymbol`) FROM `tStockUserRelation` GROUP BY `userId`;", DATABASE_URL)
    
    for relationship in allRelations:
        tempStockSymbolArray = relationship['GROUP_CONCAT(`stockSymbol`)'].split(",")

        messageToSend = "Hello! Hope you're having a great day so far.\nThe current stocks you are following are: "
        for x in range(0, len(tempStockSymbolArray)):
            messageToSend += tempStockSymbolArray[x]
            if(x != len(tempStockSymbolArray)):
                messageToSend += ", "
                
        sendDirectMessage(str(relationship['userId']), messageToSend)
        
        for symbol in tempStockSymbolArray:
            currentDataSymbolIndex = -1
            for x in range(0, len(currentData)):
                if(currentData[x][0] == symbol):
                    currentDataSymbolIndex = x
            messageToSend = "Stock: " + currentData[currentDataSymbolIndex][0] + "\n"
            messageToSend += "Company Name: " + currentData[currentDataSymbolIndex][1] + "\n"
            messageToSend += "Current Stock Price: " + str(currentData[currentDataSymbolIndex][4]) + "\n"

            if(abs(currentData[currentDataSymbolIndex][3]) < .08):
                messageToSend += "Based on the lack of relevant articles, we believe the stock will stay consistent today.\n"
            elif(currentData[currentDataSymbolIndex][3] < 0):
                messageToSend += "According to the top headlines in recent news, we predict that the value of the stock will decrease"
                if(abs(currentData[currentDataSymbolIndex][3]) > 4):
                    messageToSend += " significantly.\n"
                elif(abs(currentData[currentDataSymbolIndex][3]) > 2):
                    messageToSend += " moderately.\n"
                else:
                    messageToSend += " slightly.\n"
            elif(currentData[currentDataSymbolIndex][3] > 0):
                messageToSend += "According to the top headlines in recent news, we predict that the value of the stock will increase"
                if(abs(currentData[currentDataSymbolIndex][3]) > 4):
                    messageToSend += " significantly.\n"
                elif(abs(currentData[currentDataSymbolIndex][3]) > 2):
                    messageToSend += " moderately.\n"
                else:
                    messageToSend += " slightly.\n"
            
            for articleInfo in currentData[currentDataSymbolIndex][2]:
                messageToSend += articleInfo[0]['title'] + " --- " + articleInfo[0]['url'] + "\n"
            sendDirectMessage(str(relationship['userId']), messageToSend)

def postDaily():
    #Query for all the stocks we need to get information for
    requestedStocks = symbolArray
    currentData = getCurrentData(requestedStocks)
    #print(currentData)

    newlist = sorted(currentData, key=lambda x: abs(x[3]), reverse=True)
    mostVolatileStocks = []
    for x in range(0, 5):
        mostVolatileStocks.append(newlist[x])

    messageToSend = "Hello! Hope everyone is having a great day so far.\n Here are the top five stocks that we believe will be the most volatile throughout the course of the day! Please let us know what you think!\n"
    postToTwitter(messageToSend)
    for item in mostVolatileStocks:
        messageToSend = "Stock: " + item[0] + "\n"
        messageToSend += "Company Name: " + item[1] + "\n"
        messageToSend += "Current Stock Price: " + str(item[4]) + "\n"
        
        if(item[3] < 0):
            messageToSend += "According to the top headlines in recent news, we predict that the value of the stock will decrease"
            if(abs(item[3]) > 4):
                messageToSend += " significantly.\n"
            elif(abs(item[3]) > 2):
                messageToSend += " moderately.\n"
            else:
                messageToSend += " slightly.\n"
        elif(item[3] > 0):
            messageToSend += "According to the top headlines in recent news, we predict that the value of the stock will increase"
            if(abs(item[3]) > 4):
                messageToSend += " significantly.\n"
            elif(abs(item[3]) > 2):
                messageToSend += " moderately.\n"
            else:
                messageToSend += " slightly.\n"
            
        #for articleInfo in item[2]:
        #    messageToSend += articleInfo[0]['title'] + " --- " + articleInfo[0]['url'] + "\n"
        postToTwitter(messageToSend)
            
    
    
if(__name__ == "__main__"):
    print("Starting up!\n")

    print("Initializing the Twitter API\n")
    initTwitterAPI()
    print("Done initializing the Twitter API\n")

    print("Initializing the Google Natural Language API\n")
    initGoogleAPI()
    print("Done initializing the Google Natural Language API\n")

    #sendDirectMessage("1096608162218688517","testing")

    sendDailyDirectMessage()
    #postDaily()


    
    '''
    

    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    #api = tweepy.API(auth)

    #api.update_status('Hello Python Central!')

    #print(api.direct_messages())

    
    #print(getNewsArticles(stockNameArray[0]))
    #print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    #defineAPI()
    #getFeed()
    #print(NEWS_ARTICLE_ENDPOINT)
    #At 10:00 AM each day, we will call this method.
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/jeremy/Desktop/TwitterStockSubscription/studious-metric-231904-9ac90bc14eb9.json"
    #init()
    #currentData = getCurrentData()
    #for dataset in currentData:
    #    print("Stock: %s, Volatility: %i", dataset[1], dataset[3]) 


    '''
    
