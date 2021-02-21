import pymongo
from pymongo import MongoClient
import praw
import re
import csv

#database setup mongodb
client = pymongo.MongoClient("mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["meme"]
collection = db["memedata"]
post = {}
# reddit 0auth
client_id = "OZsROIAyH5bAbA"
client_secret = 'PhYFLRgpllL3ZPpdIQe3D5yhRWc'
username = "DK00167"
password = "98766789"
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username, password=password,user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")

def meme_file_creator():
    
    page_list = ['funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                'SaimanSays/', 'wholesomememes', 'IndianMeyMeys', 'indiameme', 'desimemes', 'Tinder', '2meirl4meirl',
                'ComedyCemetery', 'terriblefacebookmemes']
    field = ['MemePage', 'Memetitle', 'MemeUrl']
    j = 1
    for meme_page in page_list:
        memes = reddit.subreddit(meme_page)
        top_memes = memes.top('week')
        i = 0  # counter for selcting 5 memes
        for memes in top_memes:
            if re.search("^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg)$", memes.url):
                post  = {"_id": j ,"memepage":meme_page , "memetitle": memes.title , "memeurl":memes.url,"count":0}
                collection.insert_one(post)
                i,j = i+1 , j+1
            if i == 5: break #number of memes per page
    print('done')
