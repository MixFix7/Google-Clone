from django.shortcuts import render
from googleapiclient.discovery import build
from googleApp.key import api_key

cse_id = '000888210889775888983:y9tkcjel090'


def home(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET["search"]
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id).execute()
    # avatars = res['items']['pagemap']['cse_image'][0]
   # print(avatars)
    return render(request, 'search.html', {'query': query, 'res': res})

