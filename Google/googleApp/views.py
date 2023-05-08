from django.shortcuts import render, redirect
from googleapiclient.discovery import build
from googleApp.key import api_key2, api_key3, cx1, cx2, api_keyimg, api_key4, openai_key
from google_images_search import GoogleImagesSearch
import requests
from gpytranslate import SyncTranslator
from googleApp.models import Chat_with_GPT
import openai

openai.api_key = openai_key

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


def chat_page(request):
    chat_history = Chat_with_GPT.objects.all()
    return render(request, 'chat.html', {'chat_history': chat_history})

def send_message(request):
    chat_history = Chat_with_GPT.objects.all()
    get_message = request.POST.get("chattitle")
  #      get_profession = request.POST.get("profession")

    #    pattern = f"You professional {get_profession}. Give answer on human message: {get_message}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=get_message,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    AI_ANSVER = response['choices'][0]['text']
    Chat_with_GPT.objects.create(user_message=get_message, gpt_message=AI_ANSVER)
    return redirect('chat')



def clear_chat_page(request):
    if request.method == "GET":

        Chat_with_GPT.objects.all().delete()
        return redirect('chat')



