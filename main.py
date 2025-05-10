import requests
from bs4 import BeautifulSoup

import json

HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}

# try:
#     response = requests.get(url, headers=HEADERS)
#     response.raise_for_status() # check if the request is successful
#     return response.text
# except requests.RequestException as e:
#     print(f"An error occured: {e}")

site_url = "https://www.cuisine-libre.org/"
url = "https://www.cuisine-libre.org/pouding-chomeur"


def reformat(string):
    return string.replace("\xa0", " ").replace("\n", " ").strip()

def get_time_recette(recipe_infos_p, classe_name):
    span = recipe_infos_p.find("span", class_=classe_name)
    time_prepation = span.find("time").text if span else ""
    return reformat(time_prepation).replace("?","")



def get_cake_page(url):
    """ get web page html"""

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status() # check if the request is successful
        return response.text
    except requests.RequestException as e:
        print(f"An error occured: {e}")


def get_cake_data(url):
    html = get_cake_page(url)
    soup = BeautifulSoup(html, "html.parser")
    
    titre = reformat(str(soup.find("h1").contents[0]))
    recipe_infos_p = soup.find('p', id='recipe-infos')

    # duree_preparation = recipe_infos_p.find("time", class_=lambda x: x and x.startswith("crayon article-duree_preparation")).text

    # info
    duree_preparation = get_time_recette(recipe_infos_p, "duree_preparation")
    duree_cuisson = get_time_recette(recipe_infos_p, "duree_cuisson")
    duree_repos = get_time_recette(recipe_infos_p, "duree_repos")
    a_methode = recipe_infos_p.find("a", href="four")
    methode_cuisson = a_methode.text if a_methode else ""

    infos = {"duree_preparation": duree_preparation,
             "duree_cuisson": duree_cuisson,
             "duree_repos": duree_repos,
             "methode_cuisson": methode_cuisson}

    # ingredient
    ingredient_div = soup.find("div", id="ingredients")
    ingredient_li = ingredient_div.find_all("li", class_="ingredient")
    ingredient = [reformat(i.text) for i in ingredient_li if not i.find("i")]

    # preparation
    

    etape_div = soup.find("div", id="preparation")
    items_preparation = etape_div.find_all("p")
    if len(items_preparation) == 0:
        items_preparation = etape_div.find_all("li")
    etapes = [reformat(i.text) for i in items_preparation]

    
    recette = {"titre": titre,
               "infos": infos,
               "ingredients": ingredient,
               "etapes":etapes}
    
    return recette

def get_list_recette(url):
    html_data = get_cake_page(url)
    soup = BeautifulSoup(html_data, "html.parser")
    cake_ul = soup.find("div", id="recettes").find_all("div", class_="item")

    list_recette = []

    for item in cake_ul:
        titre = reformat(item.find("strong").text)
        url_ = site_url+item.find("a")['href']
        url_image = site_url+item.find("img")['src']
        index_int = url_image.find("?")
        url_image = url_image[:index_int] if index_int != - 1 else url_image

        recette = get_cake_data(url_)

        items = {"titre":titre, "url":url_, "url_image":url_image, "recette":recette}
        list_recette.append(items)

    return list_recette

list_recette = get_list_recette("https://www.cuisine-libre.org/boulangerie-et-patisserie?mots%5B%5D=83&max=100")

list_recette_json = json.dumps(list_recette)

with open("recette.json", "w") as f:
    f.write(list_recette_json)


# print(list_recette)
# print(len(list_recette))
# get_cake_data(get_cake_page(url))
    




