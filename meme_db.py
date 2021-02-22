import random
import pymongo
from pymongo import MongoClient
import json
client = pymongo.MongoClient("mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["meme"]
collection = db["memedata"]
max_count = list(collection.find().sort("count",-1).limit(1))[0]['count'] #get max count
def send_meme(x=0):
    total_memes = collection.estimated_document_count() #total_meme
    random_number = random.randint(1,total_memes) #random meme by id 
    meme_id = list(collection.find({"_id":random_number}))#cursor object to list
    meme_data = meme_id[0] #list ka first element = dict 
    if x==0:
        if meme_data['count'] == max_count:
            send_meme(x=1) # just increase the probality of not geting same meme by 1/(totalmeme)**2
        else:
            collection.update_one({ "_id" : random_number },{ "$set" : { "count":meme_data['count']+1 } })#update count
            memepage , memetitle, memeurl = meme_data['memepage'],meme_data['memetitle'] ,meme_data['memeurl']
            return memepage,memetitle,memeurl #return data
    else:
        collection.update_one({ "_id" : random_number },{ "$set" : { "count":meme_data['count']+1 } })#update count
        memepage, memetitle, memeurl = meme_data['memepage'], meme_data['memetitle'], meme_data['memeurl']
        return memepage, memetitle, memeurl  # return data

