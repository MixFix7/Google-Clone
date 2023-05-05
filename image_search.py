from google_images_search import GoogleImagesSearch
from googleApp.key import cx2, api_key3

gis = GoogleImagesSearch(api_key3, cx2)
gis.search({'q': 'машини', 'num': 20})

for image in gis.results():
    print(image.url)