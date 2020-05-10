from rest.forms import TextForm
from django.shortcuts import render
from rest_framework.views import APIView
from operations.morph.morph import MorphAnalyzer


class NormalFormHandler(APIView):

    def __init__(self):
        super().__init__()
        self.__morph = MorphAnalyzer()
        print(self.__morph)

    def get(self, request):
        return render(request, 'views/normal/form.html', {'form': TextForm()})

    def post(self, request):
        form = TextForm(request.data)
        if not form.is_valid():
            return render(request, 'views/normal/form.html', {'form': TextForm()})
        response = self.__morph.normalForm(request.data.get('word'))
        return render(request, 'views/normal/form.html', {'form': form, 'normals': response})