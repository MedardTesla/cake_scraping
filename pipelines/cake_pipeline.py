
import requests
from bs4 import BeautifulSoup
import os
import json

HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
JSON_FILE_NAME = "recette.json"


site_url = "https://www.cuisine-libre.org/"
url = "https://www.cuisine-libre.org/pouding-chomeur"

def get_cake_page(url, **kwargs):
    """ get web page html"""

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status() # check if the request is successful
        return response.text
    except requests.RequestException as e:
        print(f"An error occured: {e}")