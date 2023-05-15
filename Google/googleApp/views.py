from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .searches import search_sites, search_videos, search_images, search_images2, gpt_bot
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from googleApp.models import Chat_GPT
from django.contrib import messages



class Home(TemplateView):
    template_name = 'index.html'


class Register(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'register.html', {'form': form})






class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')



class SearchPage(View):

    def get(self, request):
        search_user = request.GET["search"]
        results_sites = search_sites(search_user)
        result_gpt = gpt_bot(search_user)
        return render(request, 'search.html', {'query': search_user, 'res': results_sites, 'resGpt': result_gpt})


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



