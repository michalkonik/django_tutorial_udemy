from django.urls import path
from pierwsza_aplikacja import views 

app_name = 'pierwsza_aplikacja_nazwa'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.CBView.as_view(), name='index'),
    path('forms', views.form_name_view, name='form_name'),
    path('other', views.OtherView.as_view(), name='other'),
    #path('other', views.other, name='other'),
    path('register', views.register, name='register'),
    path('relative_url_template', views.relative_url_template, name='relative_url_template'),
    path('logout', views.user_logout, name='logout'),
    path('special', views.special, name='special'),
    path('user_login', views.user_login, name='user_login'),
]
