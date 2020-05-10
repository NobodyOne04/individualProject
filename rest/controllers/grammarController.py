from operations.morph.morph import MorphAnalyzer
from rest_framework.views import APIView
from django.shortcuts import render
from rest.forms import TextForm


class GrammarHandler(APIView):

    def __init__(self):
        super().__init__()
        self.__morph = MorphAnalyzer()

    def get(self, request):
        return render(request, 'views/grammar/form.html', {'form': TextForm()})

    def post(self, request):
        form = TextForm(request.data)
        if not form.is_valid():
            return render(request, 'views/grammar/form.html', {'form': TextForm()})
        response = self.__morph.grammars(request.data.get('word'))
        return render(request, 'views/grammar/form.html', {'form': form, 'grammars': response})
