from django.shortcuts import render
from googleapiclient.discovery import build
from googleApp.key import api_key2, api_key3, cx1, cx2, api_keyimg
from google_images_search import GoogleImagesSearch
import requests
from gpytranslate import SyncTranslator

t = SyncTranslator()

def search_sites(query):
    service = build('customsearch', 'v1', developerKey=api_key2)
    res = service.cse().list(q=query, cx=cx1).execute()
    return res

def search_images(query):
    serviceImg = build('customsearch', 'v1', developerKey=api_key3)
    res = serviceImg.cse().list(q=query, cx=cx2, searchType='image', num=50).execute()
    return res

def search_images2(query):
    gis = GoogleImagesSearch(api_key3, cx2)
    gis.search({'q': query, 'num': 20})
    return gis.results()

def search_images3(query):
    query_en = t.translate(query, targetlanguage="en")
    url = f'https://pixabay.com/api/?key={api_keyimg}&q={query_en["text"]}&per_page=100'
    images = requests.request("GET", url)
    return images.json()

def home(request):
    return render(request, 'index.html')

def search(request):
    query_user = request.GET["search"]
    results_sites = search_sites(query_user)
    return render(request, 'search.html', {'query': query_user, 'res': results_sites})

def search_images_page(request):
    query_img = request.GET["searchimg"]
    results_images = search_images3(query_img)
    return render(request, 'search_images.html', {'query': query_img, 'resImages': results_images})

