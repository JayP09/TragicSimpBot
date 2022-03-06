import pymongo
import praw
from os import environ


class Database_oauth():

    def __init__(self):
        self.TOKEN = environ['TOKEN']
        self.OWNER_IDS = [252353540327079936, 669518518777282561]
        
        #database token
        self.db_link = environ['DB_LINK']
        self.client = pymongo.MongoClient(self.db_link)
        
        #reddit api key
        self.client_id = environ['CLIENT_ID']
        self.client_secret = environ['CLIENT_SECRET']
        self.username = environ['USERNAME']
        self.password = environ['PASSWORD']
        
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, username=self.username,
                                  password=self.password,
                                  user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
        
        #FavQs Api key
        self.ACCESS_KEY_QUOTES = environ['ACCESS_KEY_QUOTES']

    def discord_TOKEN(self):
        return self.TOKEN , self.OWNER_IDS

    def database_info(self):
        return self.client

    def oauth_info(self):
        return self.reddit

    def quote_key(self):
        return self.ACCESS_KEY_QUOTES
