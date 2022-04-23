from django.urls import path
from home.views import HomeTemplateView, AboutTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="hello"),
    path("about/", AboutTemplateView.as_view(), name="about"),
]
