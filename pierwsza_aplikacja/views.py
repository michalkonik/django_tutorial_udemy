#from tkinter import Widget
from django.shortcuts import render
from django.http import HttpResponse
from pierwsza_aplikacja.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list, 'insert_me':"Jestem wartością zmiennej 'access_records' fuck yeah !! "}

    return render(request, 'pierwsza_aplikacja/index.html', context=date_dict)


def form_name_view(request):
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success yeah")

            post_data_name = form.cleaned_data['name']
            post_data_email = form.cleaned_data['email']
            post_data_text = form.cleaned_data['text']

            print({'name': post_data_name, 'email': post_data_email, 'text': post_data_text})

            form = {'form': forms.FormName(request.POST)}
        else:
            raise forms.ValidationError("Validation failed. Fuck off")
    else:
        form = {'form': forms.FormName()}

    return render(request, 'pierwsza_aplikacja/form_page.html', context=form)


def other(request):
    return render(request, 'pierwsza_aplikacja/other.html')

def relative_url_template(request):
    return render(request, 'pierwsza_aplikacja/relative_url_template.html')

