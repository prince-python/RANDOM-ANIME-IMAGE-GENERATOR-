from django.shortcuts import render,HttpResponse
import requests
def index(request):
    data=requests.get("https://nekos.best/api/v2/neko").json()
    img=data['results'][0]["url"]
 
    return render(request,"index.html",{"img":img})
