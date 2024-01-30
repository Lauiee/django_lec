from django.contrib import admin

# Register your models here.
from django.contrib import admin

from pages.models import TeamInfo, Hello

admin.site.register(TeamInfo)
admin.site.register(Hello)