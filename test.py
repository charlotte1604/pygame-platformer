import requests

def check_word(word):
    response=requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word).json()
    if isinstance(response,list):
        return True
    return False

print(check_word("shjda"))