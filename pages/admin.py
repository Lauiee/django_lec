from django.contrib import admin

# Register your models here.
from django.contrib import admin

from pages.models import TeamInfo, Hello, Player

admin.site.register(TeamInfo)
admin.site.register(Hello)
admin.site.register(Player)