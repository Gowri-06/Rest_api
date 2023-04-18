from django.contrib import admin
from . models import * 

admin.site.register([Article,Interest,City,Person,PersonAddress])
