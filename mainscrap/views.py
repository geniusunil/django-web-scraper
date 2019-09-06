from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import csv
import re

def index(request):
    if request.method == "POST":
        url  = request.POST.get('url', '')

        r = requests.get(url)           
        soup = BeautifulSoup(r.content, features="lxml")    

        p_name = soup.find_all("h2",attrs={"class": "a-size-mini"})

        p_price = soup.find_all("span",attrs={"class": "a-price-whole"})


        with open('product_file.csv', mode='w') as product_file:
            product_writer = csv.writer(product_file)
            for name,price in zip(p_name,p_price):
                product_writer.writerow([name.text, price.text])   

        for name,price in zip(p_name,p_price):
            print(name.text)


    return render(request, 'index.html',{'p_name':p_name})
