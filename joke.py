import requests
import urllib.request as url 

def joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/" + word 
    return ((requests.get(link)).json())["delivery"]    