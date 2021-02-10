import requests

def fact():

    fact = (requests.get("https://uselessfacts.jsph.pl/random.json?language=en")).json()['text'] #return fact
    return fact
