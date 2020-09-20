from django.urls import path
from . import views

app_name = 'palaute'
urlpatterns = [
    # ex: /palaute/
    path('', views.index, name='index'),
    # ex: /palaute/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /palaute/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /palaute/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]