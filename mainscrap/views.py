from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
import requests
from bs4 import BeautifulSoup
import csv
import re
from . import forms
from . import models
from .models import Data
from . forms import scrap
import pandas as pd 
from urllib.parse import urlencode

def index(request):
    if request.method == "POST":

        url  = request.POST.get('url', '')

        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="lxml")
        p_name = soup.find_all("h2",attrs={"class": "a-size-mini"})
        p_price = soup.find_all("span",attrs={"class": "a-price-whole"})
        p_image = soup.findAll('img', {'class':'s-image','src':re.compile('.jpg')})

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product_file.csv"'


        for name,price,image in zip(p_name,p_price,p_image):
            writer = csv.writer(response)
            row = writer.writerow([image['src'],name.text, price.text,])

            name_data  = [data.text for data in p_name]
            price_data = [data.text for data in p_price]
            image_data = [data['src'] for data in p_image]
            dec = {'name':name_data, 'price':price_data, 'image':image_data, 'url':url}

        
        return render(request,'data.html', dec)

    return render(request, 'index.html')


def data(request):

    url  = request.POST.get('url', '')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")
    p_name = soup.find_all("h2",attrs={"class": "a-size-mini"})
    p_price = soup.find_all("span",attrs={"class": "a-price-whole"})
    p_image = soup.findAll('img', {'class':'s-image','src':re.compile('.jpg')})

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product_file.csv"'


    for name,price,image in zip(p_name,p_price,p_image):
        writer = csv.writer(response)
        row = writer.writerow([image['src'],name.text, price.text,])

        name_data  = [data.text for data in p_name]
        price_data = [data.text for data in p_price]
        image_data = [data['src'] for data in p_image]

    return response
    

def upload(request):
    if request.method == "POST":

        filename = request.POST.get('filename','')
        csv_file = request.POST.get('csv_file','')
        user     = request.user
        data     = Data(filename=filename, csv_file=csv_file, user=user)
        data.save()
    return render(request, 'upload.html')
