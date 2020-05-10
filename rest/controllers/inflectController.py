from django.shortcuts import render
from rest_framework.views import APIView
from operations.morph.morph import MorphAnalyzer
from rest.forms import TextForm, POSSelector, NumSelector


class InflectHandler(APIView):

    def __init__(self):
        super().__init__()
        self.__morph = MorphAnalyzer()

    def get(self, request):
        return render(request, 'views/inflect/form.html', {'form': TextForm(),
                                                           'pos': POSSelector(),
                                                           'num': NumSelector()})

    def post(self, request):
        form = TextForm(request.data)
        if not form.is_valid():
            return render(request, 'views/inflect/form.html', {'form': TextForm(),
                                                               'pos': POSSelector(),
                                                               'num': NumSelector()})
        response = self.__morph.inflect(request.data.get('word', ''), dict(request.data)['services'])
        return render(request, 'views/inflect/form.html', {'form': form,
                                                           'inflected': response,
                                                           'pos': POSSelector(),
                                                           'num': NumSelector()})
