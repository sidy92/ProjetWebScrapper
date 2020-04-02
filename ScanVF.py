import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

Site="https://www.scan-vf.net/"

def Navigate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    ListeLiens = RecupListeLiens(soup)
    return [soup,ListeLiens]


def RecupListeLiens(soup):
    ListeLiens = []
    Img = soup.findAll('img')
    for item in Img:
        if 'class' in item.attrs and item['class'] == ['img-responsive']:
            ListeLiens.append(item['data-src'])
    return ListeLiens

def Next(soup,url):
    numero = numero(url)
    urlsansnum = urlsansnum(url)
    NextUrl = urlsansnum + str(numero+1)
    if RecupListeLiens(soup) == []:
        NextUrl="Fin du Manga"
    else:
        print(NextUrl)
    return NextUrl




def numero(url):
    numero=url.split('chapitre-')[-1]
    return int(numero)


def urlsansnum(url):
    urlsansnum = url.split(str(isole(url)))[0]
    return urlsansnum