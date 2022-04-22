#from tkinter import Widget
from django.shortcuts import render
from pierwsza_aplikacja.models import Topic, UserProfileInfo, Webpage, \
        AccessRecord, UserProfileInfo, School, Student
from . import forms


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView, ListView, DetailView


class CBView(View):
    def get(self, request):
        #return HttpResponse("Class Base Views are fucking cool !")
        webpages_list = AccessRecord.objects.order_by('date')
        date_dict = {'access_records': webpages_list, 'insert_me':"Jestem wartością zmiennej 'access_records' fuck yeah !! "}
        return render(request, 'pierwsza_aplikacja/index.html', context=date_dict)



# Belov 'function based view', which has been replaced with above Class Based View
'''def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list, 'insert_me':"Jestem wartością zmiennej 'access_records' fuck yeah !! "}

    return render(request, 'pierwsza_aplikacja/index.html', context=date_dict)'''


class OtherView(TemplateView):
    template_name = "pierwsza_aplikacja/other.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION YEAH! :o'
        return context


#replaced with the above class ^^
'''def other(request):
    return render(request, 'pierwsza_aplikacja/other.html')'''


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")



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


def relative_url_template(request):
    return render(request, 'pierwsza_aplikacja/relative_url_template.html')

def registration(request):
    return render(request, 'pierwsza_aplikacja/registration.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print("coś tutaj nie zabanglało")
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'pierwsza_aplikacja/registration.html', 
                            {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered': registered})

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'pierwsza_aplikacja/login.html', {})


class SchoolList(ListView):
    model = School()


class SchoolDetailView(DetailView):
    model = School
    template_name = 'pierwsza_aplikacja/school_detail.html'


    