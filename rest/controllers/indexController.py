from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest.forms import SelectorForm


class IndexHandler(APIView):

    def __init__(self):
        super().__init__()

    def get(self, request):
        return render(request, 'views/index/base.html', {'selector': SelectorForm()})

    def post(self, request):
        if request.data.get('services', ''):
            return redirect(request.data.get('services'))
        return render(request, 'views/index/base.html', {'selector': SelectorForm()})
