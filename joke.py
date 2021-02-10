import requests
import urllib.request as url 

def joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/" + word #joke api
    print(link)
    return ((requests.get(link)).json())["delivery"]    #return joke

