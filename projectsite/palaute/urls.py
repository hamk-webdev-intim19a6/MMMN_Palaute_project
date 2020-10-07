from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'palaute'
urlpatterns = [
    # ex: /palaute/
    path('', views.index, name='index'),
    # ex: /palaute/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /palaute/5/results/
    path('<int:question_id>/results/', staff_member_required(views.results.as_view()), name='results'),
    # ex: /palaute/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('index/', views.index, name="index"),
]