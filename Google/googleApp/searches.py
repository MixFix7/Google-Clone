from googleapiclient.discovery import build
from .key import api_key2, api_key3, cx1, cx2, api_keyimg, api_key4, openai_key
import requests
from gpytranslate import SyncTranslator

from openai import OpenAI
client = OpenAI(api_key=openai_key)

t = SyncTranslator()

def gpt_bot(gpt_message):
    print(gpt_message)
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-0613",
    #     prompt=history,
    #     temperature=0.25,
    #     max_tokens=1000,
    #     top_p=1.0,
    #     frequency_penalty=0.5,
    #     presence_penalty=0.0,
    # )
    # ai_answer = response['choices'][0]['text']
    # return ai_answer

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": gpt_message},
        ]
    )
    print(response.choices[0].message.content)

    return response.choices[0].message.content

# def chat_with_gpt(prompt, max_tokens=50):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=max_tokens
#     )
#     return response.choices[0].text.strip()


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