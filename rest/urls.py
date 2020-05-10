from django.urls import path
from rest.controllers import indexController, inflectController, grammarController, normalController

urlpatterns = [
    path('', indexController.IndexHandler.as_view()),
    path('grammar', grammarController.GrammarHandler.as_view()),
    path('normal', normalController.NormalFormHandler.as_view()),
    path('inflect', inflectController.InflectHandler.as_view()),
]