import requests
import urllib.request as url 

def joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/" + word #joke api
    print(link)
    return ((requests.get(link)).json())["delivery"]    #return joke


def fact():
    
    fact = (requests.get("https://uselessfacts.jsph.pl/random.json?language=en")).json()['text'] #return fact
    return fact
