import requests
import urllib.request as url 

def get_joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/" + word #joke api
    print(link)
    try:
        return ((requests.get(link)).json())["delivery"]    #return joke 1line and 2line
    except :
        return ((requests.get(link)).json())["joke"] #return joke 1liner
