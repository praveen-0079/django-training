from django.urls import path
from news import views

urlpatterns = [
    path("<int:year>/", views.year_archive),
    # path("<int:year>/<int:month>/", views.month_archive),
    # path("<int:year>/<int:month>/<int:pk>/", views.article_detail),

    path('create/', views.ArticleCreateView.as_view(), name='article-create'),

]
