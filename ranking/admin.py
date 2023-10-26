from django.contrib import admin
from ranking.models import Ranking, Comment

class RankingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ranking._meta.fields]
    list_display_links = ['user']
    
admin.site.register(Ranking, RankingAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    list_display_links = ['id']

admin.site.register(Comment, CommentAdmin)