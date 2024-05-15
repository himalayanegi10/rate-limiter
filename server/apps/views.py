from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .redis import redis_client


class IndexView(View):
    def get(self, request, *args, **kwargs):
        counter = redis_client.get("counter")
        context = {
            'number_of_clicks': counter,
        }
        return render(request, 'index.html', context=context)
