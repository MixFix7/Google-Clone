from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .searches import search_sites, search_videos, search_images, gpt_bot
from .models import *


class Home(TemplateView):
    template_name = 'index.html'


class SearchPage(View):

    def get(self, request):
        search_user = request.GET["search"]
        results_sites = search_sites(search_user)
       # result_gpt = gpt_bot(search_user)
        return render(request, 'search.html', {'query': search_user, 'res': results_sites}) # 'resGpt': result_gpt,


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



class ChatMessages(View):

    def get(self, request):
        username = request.user.username
        history = ChatGPTHistory.objects.filter(name=username)
        return render(request, 'chat.html', {'history': history})



class Send_message(View):

    def post(self, request):
        username = request.user.username
        get_message = request.POST.get("chttitle")
        bot_message = gpt_bot(get_message)
        ChatGPTHistory.objects.create(name=username, gpt_message=bot_message, user_message=get_message)
        return redirect('chat')


class Delete_chat(View):

    def get(self, request):
        username = request.user.username
        ChatGPTHistory.objects.filter(name=username).delete()
        return redirect('chat')






