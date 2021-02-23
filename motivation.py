import random
import requests
from rake_nltk import Rake
from os import environ
import random
import pymongo
from pymongo import MongoClient
import json
client = pymongo.MongoClient("mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["meme"]
collection = db["quotes"]

CATEGORY = ['motivation', 'inspiration', 'inspire', 'motivational', 'productive']
ACCESS_KEY_QUOTES = '96e7fd9bbc2a1bc1d2f8144ef0dbb488'

def update_db(quote,author,oneCat,id_value):    
    status = collection.find_one({'quote':quote})
    if status is None:
        post = {"_id":id_value+1,'quote':quote,'author':author,'Category':oneCat,'up':0 ,'down':0 }
        collection.insert_one(post)
        return quote , author
    else:
        collection.update_one({ "_id" : status['_id'] },{ "$set" : { "count":status['count']+1 } })
        return quote ,author

def quotes_fav(oneCat=None):
    if oneCat == None:
        oneCat = random.choice(CATEGORY)
        quotes_fav(oneCat)
    if oneCat in CATEGORY:
        id_value = collection.estimated_document_count()
        response = requests.get('https://favqs.com/api/quotes/',
                                        params={'filter':oneCat},
                                        headers={'Authorization':'Token token='+ ACCESS_KEY_QUOTES},verify=False)
        quote_list_json = response.json()
        quote = quote_list_json['quotes'][0]['body']
        author = quote_list_json['quotes'][0]['author']
        
        quote , author = update_db(quote,author,oneCat,id_value)
        return quote , author
    else:
        return 'failed' , 'invalid category'
