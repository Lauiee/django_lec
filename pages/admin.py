from django.contrib import admin

# Register your models here.
from django.contrib import admin

from pages.models import TeamInfo, Hello, Player, Stadium, Comment


class PlayerAdmin(admin.ModelAdmin):
 list_display = ['playerName', 'playerPos', 'playerBackNum']
 search_fields = ['playerName']
class CommentAdmin(admin.ModelAdmin):
 list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
 search_fields = ['author']

admin.site.register(TeamInfo)
admin.site.register(Hello)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Stadium)
admin.site.register(Comment, CommentAdmin)