from django.shortcuts import render
from googleapiclient.discovery import build
from googleApp.key import api_key, api_key3, cx1, cx2
from google_images_search import GoogleImagesSearch

def search_sites(query):
    service = build('customsearch', 'v1', developerKey=api_key)
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

def home(request):
    return render(request, 'index.html')

def search(request):
    query_user = request.GET["search"]
    results_sites = search_sites(query_user)
    results_images = search_images2(query_user)
    return render(request, 'search.html', {'query': query_user, 'res': results_sites, 'resImages': results_images})

