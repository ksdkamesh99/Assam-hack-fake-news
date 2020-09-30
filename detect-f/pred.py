import argparse
import pickle
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from textblob import TextBlob
import nltk
import re
from nltk.corpus import stopwords
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS


def model1(query):
    with open('dltokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open('dlmodel.pickle', 'rb') as handle:
        model11 = pickle.load(handle)
    
    with open('logistic.pickle', 'rb') as handle:
        model22 = pickle.load(handle)
    

    text = tokenizer.transform([query])
    prediction1 = model11.predict(text)
    prediction2 = model22.predict(text)
    
    if prediction1[0] == prediction2[0]:
	    return prediction1[0]
	
    return 2
   

def model2(query):
    with open('mltokenizer.pickle', 'rb') as handle:
        tfidf_vectorizer = pickle.load(handle)

    with open('linear_clf.pickle', 'rb') as handle:
        model = pickle.load(handle)

    text = tfidf_vectorizer.transform([query])
    prediction = model.predict(text)
    return prediction[0]

def fetchNews(query):
    temp = query.split(' ')
    temp = "+".join(temp)
    news_url = "https://news.google.com/rss/search?q={" + str(temp) + "}"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()    
    
    soup_page = soup(xml_page,"xml")
    news_list = soup_page.findAll("item")
    results = []
    for news in news_list[0:2]:
        if '2020' in news.pubDate.text:
            results.append([news.title.text, news.link.text, news.pubDate.text])

    return results

def preprocess(text):
    stopwords = nltk.corpus.stopwords.words('english')

    result = []
    for token in gensim.utils.simple_preprocess(str(text)):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3 and token not in stopwords:
            result.append(token)
        
    return " ".join(result)

def predict(query):
    print(query)
    length = len(list(query))
    
    # print(length)
    query = preprocess(query)
    print(query)

    if TextBlob(query).sentiment.polarity > 0.8:
        print("Very Positive / Fake")
        exit(0)

    elif TextBlob(query).sentiment.polarity < -0.8:
        print("Very Negative / Fake")
        exit(0) 

    prediction = ""
    if length >= 10:
        prediction = model1(query)

    else:
    	prediction = model2(query)

    news_citation = fetchNews(query)
    if len(news_citation)!=0:
    	try:
    		return prediction,(news_citation[0], news_citation[1])
    	except:
    		return prediction,news_citation[0]
    else:
    	return prediction,"No citation"
