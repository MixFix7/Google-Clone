from django.shortcuts import render, redirect, get_object_or_404
from googleapiclient.discovery import build
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from googleApp.key import api_key2, api_key3, cx1, cx2, api_keyimg, api_key4, openai_key
from google_images_search import GoogleImagesSearch
import requests
from gpytranslate import SyncTranslator
from googleApp.models import Chat_GPT
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


def gpt_bot(history):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=history,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    ai_answer = response['choices'][0]['text']
    return ai_answer


class Home(TemplateView):
    template_name = 'index.html'


class SearchPage(View):
    def get(self, request):
        search_user = request.GET["search"]
        results_sites = search_sites(search_user)
        return render(request, 'search.html', {'query': search_user, 'res': results_sites})


class SearchImages(View):
    def get(self, request):
        query_img = request.GET["searchimg"]
        results_images = search_images(query_img)
        return render(request, 'search_images.html', {'query': query_img, 'resImages': results_images})

class SearchVideos(View):
    def get(self, request):
        query_vid = request.GET["searchVideos"]
        videos = search_videos(query_vid)
        return render(request, 'videos.html', {'query': query_vid, 'resVideos': videos})



class ChatMessages(ListView):
    model = Chat_GPT
    template_name = 'chat.html'


class Send_message(View):
    def post(self, request):
        get_message = request.POST.get("chttitle")
        bot_message = gpt_bot(get_message)
        Chat_GPT.objects.create(gpt_message=bot_message, user_message=get_message)
        return redirect('chat')


class Delete_chat(View):
    def get(self, request):
        Chat_GPT.objects.all().delete()
        return redirect('chat')



