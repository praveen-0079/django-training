from django.shortcuts import render, HttpResponse
from news.models import Article


def home(request):
    return render(request, "index.htm")


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "year_archive.html", context)

