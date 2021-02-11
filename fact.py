import requests
import random

def fact():

    fact = (requests.get("https://uselessfacts.jsph.pl/random.json?language=en")).json()['text'] #return fact
    return fact
    
def number_fact():
    #facts about number eg:date,year or any random number
    list_of_options = ["year","date","trivia"]
    word = random.choice(list_of_options)
    final_link = "http://numbersapi.com/random/" + word +  "?json"
    fact = (requests.get(final_link)).json()['text']
    return fact


