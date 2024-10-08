from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse
from news.models import Article
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def home(request):
    return render(request, "index.htm")


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "year_archive.html", context)


class ArticleCreateView(CreateView):
    model = Article
    fields = "__all__"  # Fields to be included in the form
    template_name = 'article_form.html'  # Template to render
    success_url = reverse_lazy('article-create')  # URL to redirect after successful form submission

    def get_form(self, *args,**kwars) -> BaseModelForm:
        form = super().get_form()
        print(form.as_p())    
        return form
