from django.urls import path

from morphology.adapters.inbound.web import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("normal", views.NormalView.as_view(), name="normal"),
    path("grammar", views.GrammarView.as_view(), name="grammar"),
    path("inflect", views.InflectView.as_view(), name="inflect"),
]
