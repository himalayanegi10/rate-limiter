from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'number_of_clicks': 0,
        }
        return render(request, 'index.html', context=context)
