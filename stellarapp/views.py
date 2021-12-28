from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import Post

class HomePageView(TemplateView):
  template_name = 'home.html'

class IndexView(TemplateView):
  template_name = 'index.html'

class CategoriesView(TemplateView):
  template_name = "categories.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["post"] = Post.postobjects.all()
    return context