import requests
import random
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["meme"]
collection = db["quotes"]
# CATEGORY = ['motivation', 'inspiration', 'inspire', 'motivational', 'productive']
CATEGORY = ['MOTIVATION', 'INSPIRATION', 'INSPIRE', 'MOTIVATIONAL', 'PRODUCTIVE']
ACCESS_KEY_QUOTES = '96e7fd9bbc2a1bc1d2f8144ef0dbb488'
id_value = collection.estimated_document_count()


def update_db(quote, author, oneCat):
    status = collection.find_one({'quote': quote})
    if status is None:
        post = {"_id": id_value + 1, "quote": quote, "author": author, "Category": oneCat, "up": 0, "down": 0,
                "count": 1}
        collection.insert_one(post)
    else:
        collection.update_one({"_id": status['_id']}, {"$set": {"count": status['count'] + 1}})


def quotes_fav(oneCat=None):
    if oneCat is None:
        oneCat = random.choice(CATEGORY)
        quotes_fav(oneCat)
    if oneCat in CATEGORY:
        response = requests.get('https://favqs.com/api/quotes/',
                                params={'filter': oneCat},
                                headers={'Authorization': 'Token token=' + ACCESS_KEY_QUOTES}, verify=False)
        quote_list_json = response.json()
        quote = quote_list_json['quotes'][0]['body']
        author = quote_list_json['quotes'][0]['author']
        update_db(quote, author, oneCat)
        return quote, author
    else:
        return 'failed', 'invalid category'

def random_quote_fav():
    """
    Fetches quote of the Day
    returns a list of quote and author
    """
    response = requests.get('https://favqs.com/api/qotd',verify=False)
    print(response.json())
    quote_random = response.json()['quote']['body']
    quote_author = response.json()['quote']['author']
    return quote_random,quote_author

print(random_quote_fav())
