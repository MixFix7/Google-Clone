from django.shortcuts import render
from googleapiclient.discovery import build
from googleApp.key import api_key2, api_key3, cx1, cx2, api_keyimg, api_key4
from google_images_search import GoogleImagesSearch
import requests
from gpytranslate import SyncTranslator

t = SyncTranslator()

def search_sites(query):
    service = build('customsearch', 'v1', developerKey=api_key2)
    res = service.cse().list(q=query, cx=cx1).execute()
    return res

def search_images2(query):
    serviceImg = build('customsearch', 'v1', developerKey=api_key3)
    res = serviceImg.cse().list(q=query, cx=cx2, searchType='image').execute()
    return res

def search_images(query):
    query_en = t.translate(query, targetlanguage="en")
    url = f'https://pixabay.com/api/?key={api_keyimg}&q={query_en["text"]}&per_page=200'
    images = requests.request("GET", url)
 #   if images.json() == "<Response [200]>":
 #       images = search_images2(query)
    return images.json()

def search_videos(query):
    youtube = build('youtube', 'v3', developerKey=api_key4)

    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=50
    ).execute()

    return search_response


def home(request):
    return render(request, 'index.html')

def search(request):
    query_user = request.GET["search"]
    results_sites = search_sites(query_user)
    return render(request, 'search.html', {'query': query_user, 'res': results_sites})

def search_images_page(request):
    query_img = request.GET["searchimg"]
    results_images = search_images(query_img)
    return render(request, 'search_images.html', {'query': query_img, 'resImages': results_images})

def search_videos_page(request):
    query_vid = request.GET["searchVideos"]
    videos = search_videos(query_vid)
    return render(request, 'videos.html', {'query': query_vid, 'resVideos': videos})

