__author__ = 'johnh.evans'

from django.contrib import admin

from models import Tech, TechPerson


admin.site.register(Tech)
admin.site.register(TechPerson)