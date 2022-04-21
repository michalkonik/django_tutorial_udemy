from django.urls import path
from pierwsza_aplikacja import views 

app_name = 'pierwsza_aplikacja_nazwa'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms', views.form_name_view, name='form_name'),
    path('other', views.other, name='other'),
    path('relative_url_template', views.relative_url_template, name='relative_url_template'),
]
