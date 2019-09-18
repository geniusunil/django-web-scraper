from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import csv
import re
from . import forms
from . import models
from .models import Data
from . forms import scrap
from django_cron import CronJobBase, Schedule

def index(request):
    if request.method == "POST":

        url  = request.POST.get('url', '')

        r = requests.get(url)           
        soup = BeautifulSoup(r.content, features="lxml")    
        p_name = soup.find_all("h2",attrs={"class": "a-size-mini"})
        p_price = soup.find_all("span",attrs={"class": "a-price-whole"})

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product_file.csv"'

        for name,price in zip(p_name,p_price):
            writer = csv.writer(response)
            writer.writerow([name.text, price.text])

        return response


    return render(request, 'index.html')

    

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1440

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'my_app.my_cron_job'

#     def do(self):