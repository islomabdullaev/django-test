from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "home.html"


class AboutTemplateView(TemplateView):
    template_name = "about.html"
