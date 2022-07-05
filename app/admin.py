from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)





