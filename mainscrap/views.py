from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import csv
import re
from . import forms

def index(request):
    if request.method == "POST":
        
        url  = request.POST.get('url', '')
        r = requests.get(url)           
        soup = BeautifulSoup(r.content, features="lxml")    
        p_name = soup.find_all("h2",attrs={"class": "a-size-mini"})
        p_price = soup.find_all("span",attrs={"class": "a-price-whole"})

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product_filename.csv"'
        
        for name,price in zip(p_name,p_price):
            writer = csv.writer(response)
            writer.writerow([name.text, price.text])

        return response


    return render(request, 'index.html')