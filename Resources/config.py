import pymongo
import praw


class Database_oauth():

    def __init__(self):
        self.TOKEN = 'ODA4Njk1NTQyNTAxNzM2NDc5.YCKSag.ZfYS6EGmD2xHtvN3BwfM9ogjdQE'
        self.OWNER_IDS = [252353540327079936, 669518518777282561]
        self.db_link = "mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.db_link)
        
        self.client_id = "OZsROIAyH5bAbA"
        self.client_secret = 'PhYFLRgpllL3ZPpdIQe3D5yhRWc'
        self.username = "DK00167"
        self.password = "98766789"
        
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, username=self.username,
                                  password=self.password,
                                  user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
        
        self.ACCESS_KEY_QUOTES = '96e7fd9bbc2a1bc1d2f8144ef0dbb488'

    def discord_TOKEN(self):
        return self.TOKEN , self.OWNER_IDS

    def database_info(self):
        return self.client

    def oauth_info(self):
        return self.reddit

    def quote_key(self):
        return self.ACCESS_KEY_QUOTES
