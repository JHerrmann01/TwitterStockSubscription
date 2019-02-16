import twitter
import json
import requests
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from yahoofinancials import YahooFinancials


symbolArray = ["MSFT", "AAPL", "GOOGL", "GOOG", "FB", "INTC", "CSCO", "ORCL", "SAP", "ADBE",
		"IBM", "CRM", "AVGO", "TXN", "NVDA", "VMW", "ADP", "QCOM", "INTU", "ITW", "BIDU", "MU",
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
NEWS_ARTICLE_ENDPOINT = "https://newsapi.org/v2/top-headlines" + "?apiKey=" + NEWS_ARTICLE_API_KEY + "&sortBy=popularity" + "&q=";

api = None
client = None

def defineAPI():
    global api
    api = twitter.Api(consumer_key="Aj53Yg5ijyCb0v6KxtunaIxV8",
                  consumer_secret="VQb5UMxl2z3tryabee4s8fyh39VpzuY4yN9ThAGs3Uwd4voiha",
                  access_token_key="907456144297295872-wPrALDxqJiWjpe92JMUGlbft30kNqeH",
                  access_token_secret="eHqZFhhM13ukT4ttJj7emBl6vE6wDCbZnIY6jRS5IdyCn")

def postToTwitter(Message):
    global api
    api.PostUpdate(Message)

def getNewsArticles(Company):
    currentEndpoint = NEWS_ARTICLE_ENDPOINT + Company
    response = requests.get(currentEndpoint)
    response = json.loads(response.text)
    if(int(response['totalResults']) == 0):
        return([])
    return(response['articles'])

def init():
    global client
    # Instantiates a client
    client = language.LanguageServiceClient()

def analyzeArticle(Text):
    global client
    text = u'Hello, world!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    
if(__name__ == "__main__"):
    print("Starting up!")
    #print(getNewsArticles(stockNameArray[0]))
    #print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/jeremy/Desktop/studious-metric-231904-9ac90bc14eb9.json"

    
    getCurrentData

    ticker = 'AAPL'
    yahoo_financials = YahooFinancials(ticker)
    apple_net_income = yahoo_financials.get_current_price()
    print(apple_net_income)


    
    
