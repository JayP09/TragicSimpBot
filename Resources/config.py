import pymongo
import praw


class Database_oauth():

    def __init__(self):
        #discord token
        self.TOKEN = 'YOUR DISCORD BOT PUBLIC KEY HERE'
        self.OWNER_IDS = ['YOUR USER ID HERE']
        
        #database token
        self.db_link = "your Mongo database link here"
        self.client = pymongo.MongoClient(self.db_link)
        
        #reddit api key
        self.client_id = "YOUR CLIENT ID"
        self.client_secret = 'YOUR CLIENT SECRET'
        self.username = "YOUR REDDIT USERNAME"
        self.password = "YOUR REDDIT PASSWORD"
        
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, username=self.username,
                                password=self.password,
                                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
        
        #FavQs Api key
        self.ACCESS_KEY_QUOTES = 'YOUR API KEY HERE'

    def discord_TOKEN(self):
        return self.TOKEN , self.OWNER_IDS

    def database_info(self):
        return self.client

    def oauth_info(self):
        return self.reddit

    def quote_key(self):
        return self.ACCESS_KEY_QUOTES
