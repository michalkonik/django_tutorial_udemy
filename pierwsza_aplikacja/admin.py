from django.contrib import admin
from pierwsza_aplikacja.models import AccessRecord, Topic, Webpage, UserProfileInfo, School, Student

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Student)
