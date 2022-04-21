import imp
from django.contrib import admin
from pierwsza_aplikacja.models import AccessRecord, Topic, Webpage, UserProfileInfo

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)
