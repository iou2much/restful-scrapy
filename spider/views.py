#-*- coding: utf-8 -*-
from django.shortcuts import render
from spider.tasks import crawl

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import time

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def feed(request):
    if request.method == 'GET':
        res = {'time':time.time()}
        json_req='{"url": "http://istresearch.com", "appid":"testapp", "crawlid":"ABC123"}'
        crawl(json_req)
        return JSONResponse(res)
