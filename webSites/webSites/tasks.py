# Create your tasks here
from __future__ import absolute_import, unicode_literals
from .celery import app

import requests
import zipfile
from webSitesApp.models import Website, WebPage


@app.task
def download_file(url, out_path):
    r = requests.get(url)
    with open(out_path + "top-1m.csv.zip", "wb") as code:
        code.write(r.content)
    # unzipping
    zip_ref = zipfile.ZipFile(out_path + "top-1m.csv.zip", 'r')
    zip_ref.extractall(out_path)
    zip_ref.close()
    with open(out_path + "top-1m.csv") as f:
        for line in f:
            line_spl = line.split(",")
            alexa_rank = line_spl[0]
            url_read = line_spl[1]
            # print(alexa_rank)
            if Website.objects.filter(url=url_read).count() > 0:
                update_record(url_read, alexa_rank)
            else:
                add_record(url_read, alexa_rank)


@app.task
def add_record(url_read, alexa_rank):
    website = Website(url=url_read, alexa_rank=alexa_rank)
    website.save()
    make_or_no_web_page(url_read)


@app.task
def update_record(url_read, alexa_rank):
    website = Website.objects.filter(url=url_read)[0]
    website.alexa_rank = alexa_rank
    website.save()
    make_or_no_web_page(url_read)


@app.task
def make_or_no_web_page(url_read):
    # with open(out_path + "top-1m.csv") as f:
    #     for line in f:
    #         line_spl = line.split(",")
    #         url_read = line_spl[1]
    website = Website.objects.filter(url=url_read)[0]
    if WebPage.objects.filter(website=website).count() == 0:
        webpage = WebPage(website=website, url=url_read)
        webpage.save()
