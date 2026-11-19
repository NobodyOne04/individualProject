from django.urls import include, path

urlpatterns = [path("", include("morphology.adapters.inbound.web.urls"))]
