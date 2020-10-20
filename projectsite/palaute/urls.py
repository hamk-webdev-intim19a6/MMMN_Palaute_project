from django.urls import path
from . import views


app_name = 'palaute'
urlpatterns = [
    # ex: /palaute/
    # path('', views.index, name='index'),

    path('register/', views.register_page, name="register"),
    path('login', views.login_page, name="login"),
    path('', views.feedback, name="feedback"),
    path('logout/', views.logout_user, name="logout"),

]
